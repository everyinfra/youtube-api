"""YouTube API 示例（YouTube API in Python）。

  python main.py search "camping gear" --out videos.csv       # 按关键词搜视频 / search videos
  python main.py video "<视频链接>" --out video.json          # 视频详情 / video detail
  python main.py comments "<视频链接>" --out comments.csv     # 视频评论 / comments
  python main.py channel "<频道链接>"                         # 频道资料 / channel profile
  python main.py videos "<频道链接>" --out channel_videos.csv # 频道的视频 / a channel's videos
"""
import argparse

from everyinfra import fetch, report

SORTS = ["relevance", "newest", "most_viewed", "top_rated"]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search", help="按关键词搜视频 / search videos by keyword")
    s.add_argument("keyword")
    s.add_argument("--sort", choices=SORTS, help="排序 / sort order")
    v = sub.add_parser("video", help="视频详情 / one video")
    v.add_argument("url")
    c = sub.add_parser("comments", help="视频评论 / comments of one video")
    c.add_argument("url")
    c.add_argument("--sort", choices=SORTS, help="newest 最新 / popular 热门")
    ch = sub.add_parser("channel", help="频道资料 / channel profile")
    ch.add_argument("url")
    vi = sub.add_parser("videos", help="频道的视频 / a channel's videos")
    vi.add_argument("url")
    vi.add_argument("--sort", choices=SORTS, help="newest / oldest / popular")
    for x in (s, v, c, ch, vi):
        x.add_argument("--out", help="存成 .csv 或 .json / write .csv or .json")
    a = p.parse_args()

    if a.cmd == "search":
        params = {"keyword": a.keyword, **({"sort": a.sort} if a.sort else {})}
        rows, charged = fetch("search", params)
    elif a.cmd == "video":
        rows, charged = fetch("video", {"url": a.url})
    elif a.cmd == "comments":
        params = {"url": a.url, **({"sort": a.sort} if a.sort else {})}
        rows, charged = fetch("comments", params)
    elif a.cmd == "channel":
        rows, charged = fetch("profile", {"url": a.url})
    else:
        params = {"url": a.url, **({"sort": a.sort} if a.sort else {})}
        rows, charged = fetch("user_posts", params)
    report(rows, charged, a.out)


if __name__ == "__main__":
    main()
