#!/usr/bin/env bash
# Sync labels from .github/labels.yml to GitHub using the gh CLI.
# Usage: ./scripts/sync-github-labels.sh [owner/repo]
# Default repo: markheydon/ios-reminders-gtd

set -euo pipefail

REPO="${1:-markheydon/ios-reminders-gtd}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LABELS_FILE="${ROOT}/.github/labels.yml"

if ! command -v gh >/dev/null 2>&1; then
  echo "error: gh CLI is required (https://cli.github.com/)" >&2
  exit 1
fi

if [[ ! -f "${LABELS_FILE}" ]]; then
  echo "error: missing ${LABELS_FILE}" >&2
  exit 1
fi

# Retired default software labels (safe to delete if unused)
RETIRE=(bug enhancement documentation "good first issue" "help wanted")

sync_label() {
  local name="$1"
  local color="$2"
  local description="$3"

  if gh label list --repo "${REPO}" --limit 500 --json name -q '.[].name' | grep -Fxq "${name}"; then
    gh label edit "${name}" --repo "${REPO}" --color "${color}" --description "${description}"
    echo "updated: ${name}"
  else
    gh label create "${name}" --repo "${REPO}" --color "${color}" --description "${description}"
    echo "created: ${name}"
  fi
}

name=""
color=""
description=""

while IFS= read -r line || [[ -n "${line}" ]]; do
  line="${line%%#*}"
  line="$(echo "${line}" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  [[ -z "${line}" ]] && continue

  if [[ "${line}" == "- name:"* ]]; then
    if [[ -n "${name}" && -n "${color}" ]]; then
      sync_label "${name}" "${color}" "${description}"
    fi
    name="${line#- name: }"
    name="${name#\"}"
    name="${name%\"}"
    color=""
    description=""
  elif [[ "${line}" == "color:"* ]]; then
    color="${line#color: }"
  elif [[ "${line}" == "description:"* ]]; then
    description="${line#description: }"
    description="${description#\"}"
    description="${description%\"}"
  fi
done < "${LABELS_FILE}"

if [[ -n "${name}" && -n "${color}" ]]; then
  sync_label "${name}" "${color}" "${description}"
fi

echo ""
echo "Retiring legacy labels (if present)..."
for old in "${RETIRE[@]}"; do
  if gh label list --repo "${REPO}" --limit 500 --json name -q '.[].name' | grep -Fxq "${old}"; then
    if gh label delete "${old}" --repo "${REPO}" --yes 2>/dev/null; then
      echo "deleted: ${old}"
    else
      echo "skip delete ${old} (in use or not deletable)"
    fi
  fi
done

echo "Done. Labels in ${REPO} match ${LABELS_FILE}"
