#!/usr/bin/env bash
# YouTube API 的 curl 示例：所有能力都发到同一个地址，只换 action 和 params。
# curl examples for the YouTube API: every capability uses the same URL; only action and params change.
#
#   export EVERYINFRA_API_KEY=<your API key>
#   bash examples/curl.sh search "camping gear"
#   bash examples/curl.sh video "<video url>"        # search 结果里的 url / the url from a search result
#   bash examples/curl.sh comments "<video url>"
#   bash examples/curl.sh profile "<channel url>"    # search 结果里的 author_url / the author_url from a search result
#   bash examples/curl.sh user_posts "<channel url>"
set -euo pipefail
: "${EVERYINFRA_API_KEY:?Set EVERYINFRA_API_KEY first: https://everyinfra.com/docs#quickstart}"
action=${1:?"usage: bash examples/curl.sh <search|video|comments|profile|user_posts> <value>"}
value=${2:?"value: a keyword, a video url or a channel url"}

case "$action" in
  search)                                  params="{\"keyword\":\"$value\"}" ;;
  video | comments | profile | user_posts) params="{\"url\":\"$value\"}" ;;
  *) echo "unknown action: $action (use search, video, comments, profile or user_posts)" >&2; exit 2 ;;
esac

curl -sS -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"platform\":\"youtube\",\"action\":\"$action\",\"params\":$params}"
echo
