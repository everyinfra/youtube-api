# YouTube API

[English](#english) · [中文](#中文)

## English

This repo reads public YouTube data with Python or curl. You can search videos by keyword, read video details and comments, and look up a channel's profile and videos. You need one EveryInfra API key. You do not need a YouTube account or cookie. The same API also works as an MCP tool in Claude and Cursor. Billing is per call: these 5 capabilities cost $0.56 to $0.78 per 1,000 calls. Failed calls and empty results are not charged. The EveryInfra YouTube API has 21 capabilities, all listed on the platform page: <https://everyinfra.com/en/youtube-api?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### Quick start

```bash
git clone https://github.com/everyinfra/youtube-api.git
cd youtube-api
pip install -r requirements.txt
export EVERYINFRA_API_KEY=<your API key>
python main.py search "camping gear" --out videos.csv
python main.py video "<video url>" --out video.json
python main.py comments "<video url>" --out comments.csv
python main.py channel "<channel url>"
python main.py videos "<channel url>" --out channel_videos.csv
```

- Take the video link from the `url` field of a `search` result, for example https://www.youtube.com/watch?v=<video id>.
- For `channel` and `videos`, pass a channel link. Use the `author_url` from a `search` result, for example https://www.youtube.com/@<handle>.
- Without `--out`, the command prints the first 3 rows as JSON. With `--out`, it saves a .csv or .json file. The CSV has a BOM, so Excel opens it without garbled text.
- Register at everyinfra.com, then create the API key in the console. Steps: <https://everyinfra.com/en/docs?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api#quickstart>

### curl

```bash
curl -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform":"youtube","action":"search","params":{"keyword":"camping gear"}}'
```

All capabilities use the same URL. Change `action` and `params` to call another one. Examples for `video`, `comments`, `profile`, and `user_posts` are in [examples/curl.sh](examples/curl.sh).

### Claude and Cursor (MCP)

The remote MCP URL is <https://api.everyinfra.com/mcp>. Add the `Authorization: Bearer` header with your API key. EveryInfra runs the server, so you install no local program.

Claude Code:

```bash
claude mcp add --transport http everyinfra https://api.everyinfra.com/mcp --header "Authorization: Bearer <API Key>"
```

Cursor and other clients that read `mcp.json` ([examples/mcp.json](examples/mcp.json)):

```json
{
  "mcpServers": {
    "everyinfra": {
      "url": "https://api.everyinfra.com/mcp",
      "headers": {
        "Authorization": "Bearer <API Key>"
      }
    }
  }
}
```

Custom connectors in Claude on the web and desktop, and ChatGPT, accept only a URL. Enter <https://api.everyinfra.com/mcp/all>, sign in to EveryInfra when asked, and allow access. You do not need to enter a key. Full steps: <https://everyinfra.com/en/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### Price

| `action` | Per 1,000 calls |
|---|---|
| `search` | $0.78 |
| `video` | $0.56 |
| `comments` | $0.56 |
| `profile` | $0.56 |
| `user_posts` | $0.56 |

- Billing is per call, about $0.00056 to $0.00078 each. Failed calls, empty results, parameter errors, and authentication failures are not charged.
- A new account gets a $1 trial allowance, valid for 24 hours. No credit card is needed. How to claim it: <https://everyinfra.com/en/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>
- Prices for the other 16 YouTube capabilities are on the platform page: <https://everyinfra.com/en/youtube-api?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### Fields

These are the fields that the 5 capabilities returned in our test. Each meaning is the first sentence of the field's entry in the API documentation. The link under each table has the full text.

#### `search` (keyword search)

| Field | Meaning |
|---|---|
| `id` | The record's unique ID on the platform. |
| `url` | Link to the record on the platform. |
| `title` | Title. null when the platform has no titles (for example text-only posts). |
| `text` | Body text with HTML removed, returned in full and never cut short (on a few platforms the list results themselves carry only an excerpt; the platform's field notes say so). |
| `author_name` | Author's display name. |
| `author_username` | Author's username (@handle), usually usable in URLs. |
| `author_id` | Author's unique ID on the platform. |
| `author_url` | Link to the author's profile on the platform. |
| `like_count` | Likes. null means the platform or this capability does not disclose it; it is not 0. |
| `comment_count` | Comments. null means not disclosed, not 0. |
| `view_count` | Views or plays. null means not disclosed, not 0. |
| `duration` | Duration. |
| `posted_at` | Publish time in ISO 8601, UTC (for example 2026-08-07T12:34:56+00:00). |
| `thumbnail_url` | Thumbnail link, lower resolution than image_url. |
| `search_rank` | Position in this search's results, starting at 1. |
| `platform` | Source platform identifier, the same as platform in the request (for example xiaohongshu, tiktok). |

All parameters and fields: <https://everyinfra.com/en/youtube-api/search?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `video` (video details)

| Field | Meaning |
|---|---|
| `id` | The record's unique ID on the platform. |
| `url` | Link to the record on the platform. |
| `title` | Title. null when the platform has no titles (for example text-only posts). |
| `text` | Body text with HTML removed, returned in full and never cut short (on a few platforms the list results themselves carry only an excerpt; the platform's field notes say so). |
| `author_name` | Author's display name. |
| `author_username` | Author's username (@handle), usually usable in URLs. |
| `author_id` | Author's unique ID on the platform. |
| `author_url` | Link to the author's profile on the platform. |
| `like_count` | Likes. null means the platform or this capability does not disclose it; it is not 0. |
| `comment_count` | Comments. null means not disclosed, not 0. |
| `view_count` | Views or plays. null means not disclosed, not 0. |
| `duration` | Duration. |
| `posted_at` | Publish time in ISO 8601, UTC (for example 2026-08-07T12:34:56+00:00). |
| `thumbnail_url` | Thumbnail link, lower resolution than image_url. |
| `is_comments_disabled` | Whether comments are turned off. |
| `is_members_only` | Whether the video is for members only. |
| `is_paid_partnership` | Whether the video includes a paid promotion. |
| `author_follower_count` | Author's follower count. null means not disclosed. |
| `author_video_count` | Total number of videos on the channel. |
| `author_view_count` | Total views of the channel. |
| `author_created_at` | When the channel was created, ISO 8601 in UTC; absent on some results. |
| `description_links` | Links in the video description: text, url. |
| `platform` | Source platform identifier, the same as platform in the request (for example xiaohongshu, tiktok). |

All parameters and fields: <https://everyinfra.com/en/youtube-api/video?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `comments` (comments)

| Field | Meaning |
|---|---|
| `id` | The record's unique ID on the platform. |
| `text` | Body text with HTML removed, returned in full and never cut short (on a few platforms the list results themselves carry only an excerpt; the platform's field notes say so). |
| `author_name` | Author's display name. |
| `like_count` | Likes. null means the platform or this capability does not disclose it; it is not 0. |
| `reply_count` | Replies, usually replies to a comment. null means not disclosed. |
| `posted_at` | Publish time in ISO 8601, UTC (for example 2026-08-07T12:34:56+00:00). |
| `is_reply` | Whether this is a reply. |
| `platform` | Source platform identifier, the same as platform in the request (for example xiaohongshu, tiktok). |

All parameters and fields: <https://everyinfra.com/en/youtube-api/comments?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `profile` (profile or object details)

| Field | Meaning |
|---|---|
| `channel_id` | Channel ID (starts with UC). |
| `name` | Name of the object itself, for account, product and business capabilities. |
| `url` | Link to the record on the platform. |
| `bio` | Profile bio written by the account; may contain line breaks and emoji. |
| `subscriber_count` | Subscriber count. |
| `video_count` | Number of videos. |
| `view_count` | Views or plays. null means not disclosed, not 0. |
| `is_verified` | Whether the platform verified the account. null means it cannot be determined. |
| `location` | Location description passed through as is; the format varies by platform. |
| `avatar_url` | Avatar image link. |
| `banner_url` | Channel banner. |
| `created_at` | Creation time, same format as posted_at. |
| `platform` | Source platform identifier, the same as platform in the request (for example xiaohongshu, tiktok). |

All parameters and fields: <https://everyinfra.com/en/youtube-api/profile?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `user_posts` (user content)

| Field | Meaning |
|---|---|
| `id` | The record's unique ID on the platform. |
| `url` | Link to the record on the platform. |
| `title` | Title. null when the platform has no titles (for example text-only posts). |
| `text` | Body text with HTML removed, returned in full and never cut short (on a few platforms the list results themselves carry only an excerpt; the platform's field notes say so). |
| `author_name` | Author's display name. |
| `author_username` | Author's username (@handle), usually usable in URLs. |
| `author_id` | Author's unique ID on the platform. |
| `author_url` | Link to the author's profile on the platform. |
| `like_count` | Likes. null means the platform or this capability does not disclose it; it is not 0. |
| `comment_count` | Comments. null means not disclosed, not 0. |
| `view_count` | Views or plays. null means not disclosed, not 0. |
| `duration` | Duration. |
| `posted_at` | Publish time in ISO 8601, UTC (for example 2026-08-07T12:34:56+00:00). |
| `thumbnail_url` | Thumbnail link, lower resolution than image_url. |
| `author_follower_count` | Author's follower count. null means not disclosed. |
| `search_rank` | Position in this search's results, starting at 1. |
| `platform` | Source platform identifier, the same as platform in the request (for example xiaohongshu, tiktok). |
| `hashtags` | Hashtags in the text, in order of appearance; absent when there are none. |

All parameters and fields: <https://everyinfra.com/en/youtube-api/user_posts?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### FAQ

**Do I need a YouTube account or cookie to call the API?**

No. Send the `Authorization: Bearer` header with your API key. The request body holds `platform`, `action`, and the capability parameters. You do not scan a QR code, keep a login session, or open a browser.

**How much does it cost? Are failed calls charged? Is there a free allowance?**

Billing is per call, from $0.56 per 1,000 calls. Failed calls, empty results, parameter errors, and authentication failures are not charged. A new account gets a $1 trial allowance, valid for 24 hours. No credit card is needed. How to claim it: <https://everyinfra.com/en/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

**Can I connect the YouTube API to Claude or Cursor?**

Yes. The remote MCP URL is <https://api.everyinfra.com/mcp>. Add the `Authorization: Bearer` header with your API key. You install no local program. Setup for Claude, Cursor, ChatGPT, and Claude Code: <https://everyinfra.com/en/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>. An agent can then search YouTube content, read comments, and look up accounts by itself.

**What legal points apply when I use YouTube data?**

The EveryInfra Terms of Service require you to make sure your use of the data follows applicable law and the terms of the relevant platform. Do not use the data for anything illegal or anything that violates privacy or intellectual property rights. Do not use bulk scraping for harassment, fraud, or other abuse. When you use personal information such as nicknames and avatars, keep only the fields your business needs.

**Which YouTube data can I get?**

The EveryInfra YouTube API has 21 capabilities:

- keyword search
- profile or object details
- user content
- video details
- comments
- followers
- transcript
- shorts
- comment replies
- related posts
- Channel ID lookup
- community posts
- channel post
- channel post comments
- search in channel
- shorts search
- account search
- search suggestions
- video formats
- media download links
- Format stream URL

Parameters and return fields for each capability are on the platform page: <https://everyinfra.com/en/youtube-api?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### Tested

Before release, we ran the 5 commands in Quick start against the live API with this repo's code.

| Command | Time (Singapore, UTC+8) | Rows | Charged |
|---|---|---|---|
| `python main.py search "camping gear" --out videos.csv` | 2026-11-25 12:07 | 10 | $0.000778 |
| `python main.py video "<video url>" --out video.json` | 2026-11-25 12:07 | 1 | $0.000556 |
| `python main.py comments "<video url>" --out comments.csv` | 2026-11-25 12:07 | 20 | $0.000556 |
| `python main.py channel "<channel url>"` | 2026-11-25 12:07 | 1 | $0.000556 |
| `python main.py videos "<channel url>" --out channel_videos.csv` | 2026-11-25 12:08 | 10 | $0.000556 |

## 中文

本仓库用 Python 或 curl 读 YouTube 公开数据：按关键词搜视频，读视频详情和评论，查频道资料和频道视频。只需一把 EveryInfra API Key，不用 YouTube 账号和 Cookie，也能作为 MCP 工具接进 Claude、Cursor。按调用次数计费，这 5 个能力每千次 $0.56 到 $0.78，失败和空结果不收费。YouTube 共 21 个能力：<https://everyinfra.com/youtube-api?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### 快速开始

```bash
git clone https://github.com/everyinfra/youtube-api.git
cd youtube-api
pip install -r requirements.txt
export EVERYINFRA_API_KEY=<你的 API Key>
python main.py search "camping gear" --out videos.csv
python main.py video "<视频链接>" --out video.json
python main.py comments "<视频链接>" --out comments.csv
python main.py channel "<频道链接>"
python main.py videos "<频道链接>" --out channel_videos.csv
```

- 视频链接用 `search` 结果里的 `url`，形如 https://www.youtube.com/watch?v=<视频 ID>。
- `channel` 和 `videos` 传频道链接，用 `search` 结果里的 `author_url`，形如 https://www.youtube.com/@<handle>。
- 不加 `--out` 时打印前 3 条 JSON；加 `--out` 存成 .csv 或 .json。CSV 带 BOM，Excel 直接打开不乱码。
- API Key 在 everyinfra.com 注册后到控制台创建，步骤见 <https://everyinfra.com/docs?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api#quickstart>

### 用 curl 调

```bash
curl -X POST https://api.everyinfra.com/api/v1/social \
  -H "Authorization: Bearer $EVERYINFRA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform":"youtube","action":"search","params":{"keyword":"camping gear"}}'
```

所有能力都发到同一个地址，换 `action` 和 `params` 就行；`video`、`comments`、`profile`、`user_posts` 的写法见 [examples/curl.sh](examples/curl.sh)。

### 接进 Claude、Cursor（MCP）

远程 MCP 地址是 <https://api.everyinfra.com/mcp>，请求头加 `Authorization: Bearer` 和 API Key；服务器由 EveryInfra 运行，不用装本地程序。

Claude Code：

```bash
claude mcp add --transport http everyinfra https://api.everyinfra.com/mcp --header "Authorization: Bearer <API Key>"
```

Cursor 等读 `mcp.json` 的客户端（[examples/mcp.json](examples/mcp.json)）：

```json
{
  "mcpServers": {
    "everyinfra": {
      "url": "https://api.everyinfra.com/mcp",
      "headers": {
        "Authorization": "Bearer <API Key>"
      }
    }
  }
}
```

Claude 网页版和桌面版的自定义连接器、ChatGPT 只能填网址：填 <https://api.everyinfra.com/mcp/all>，连接时登录 EveryInfra 并允许，不用填 Key。完整步骤见 <https://everyinfra.com/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### 价格

| 能力 | `action` | 每千次 |
|---|---|---|
| 关键词搜索 | `search` | $0.78 |
| 视频详情 | `video` | $0.56 |
| 评论 | `comments` | $0.56 |
| 主页或对象详情 | `profile` | $0.56 |
| 用户内容 | `user_posts` | $0.56 |

- 按调用次数计费，每次约 $0.00056 到 $0.00078；失败、空结果、参数错误和鉴权失败都不收费。
- 新账号有 $1 试用额度，24 小时内有效，不用信用卡，领取方式见 <https://everyinfra.com/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>
- YouTube 其他 16 个能力的单价见平台页 <https://everyinfra.com/youtube-api?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### 返回字段

下面是这 5 个能力实测返回的字段，含义取自接口文档每条说明的第一句，完整说明在每张表下面的链接里。

#### `search`（关键词搜索）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `title` | 标题。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_username` | 作者用户名（@handle），通常可用于拼 URL。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_url` | 作者在原平台的主页链接。 |
| `like_count` | 点赞数。 |
| `comment_count` | 评论数。 |
| `view_count` | 浏览/播放数。 |
| `duration` | 时长。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `thumbnail_url` | 缩略图链接，分辨率低于 image_url。 |
| `search_rank` | 在这次搜索结果里的名次，从 1 开始。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

完整参数和字段：<https://everyinfra.com/youtube-api/search?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `video`（视频详情）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `title` | 标题。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_username` | 作者用户名（@handle），通常可用于拼 URL。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_url` | 作者在原平台的主页链接。 |
| `like_count` | 点赞数。 |
| `comment_count` | 评论数。 |
| `view_count` | 浏览/播放数。 |
| `duration` | 时长。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `thumbnail_url` | 缩略图链接，分辨率低于 image_url。 |
| `is_comments_disabled` | 是否关闭评论。 |
| `is_members_only` | 是否会员专享视频。 |
| `is_paid_partnership` | 是否含付费推广。 |
| `author_follower_count` | 作者粉丝数。 |
| `author_video_count` | 频道视频总数。 |
| `author_view_count` | 频道总播放量。 |
| `author_created_at` | 频道创建时间，ISO 8601 格式、UTC；部分结果没有。 |
| `description_links` | 视频简介里的链接：text、url。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

完整参数和字段：<https://everyinfra.com/youtube-api/video?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `comments`（评论）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `author_name` | 作者昵称（显示名）。 |
| `like_count` | 点赞数。 |
| `reply_count` | 回复数，通常用于评论的子回复。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `is_reply` | 是否为回复。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

完整参数和字段：<https://everyinfra.com/youtube-api/comments?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `profile`（主页或对象详情）

| 字段 | 含义 |
|---|---|
| `channel_id` | 频道 ID（UC 开头）。 |
| `name` | 名称。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `bio` | 个人简介，账号自己填写的文本。 |
| `subscriber_count` | 订阅数。 |
| `video_count` | 视频数。 |
| `view_count` | 浏览/播放数。 |
| `is_verified` | 是否为平台认证账号（蓝V等）。 |
| `location` | 地理位置描述，原文透传，格式随平台而异。 |
| `avatar_url` | 头像图片链接。 |
| `banner_url` | 频道横幅。 |
| `created_at` | 创建时间，格式同 posted_at。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |

完整参数和字段：<https://everyinfra.com/youtube-api/profile?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

#### `user_posts`（用户内容）

| 字段 | 含义 |
|---|---|
| `id` | 该记录在原平台上的唯一标识。 |
| `url` | 该记录在原平台上的可访问链接。 |
| `title` | 标题。 |
| `text` | 正文内容，已去除 HTML 标签，全文返回、不截断（个别平台的列表结果本身只有摘要，以该平台的字段说明为准）。 |
| `author_name` | 作者昵称（显示名）。 |
| `author_username` | 作者用户名（@handle），通常可用于拼 URL。 |
| `author_id` | 作者在原平台的唯一 ID。 |
| `author_url` | 作者在原平台的主页链接。 |
| `like_count` | 点赞数。 |
| `comment_count` | 评论数。 |
| `view_count` | 浏览/播放数。 |
| `duration` | 时长。 |
| `posted_at` | 发布时间，ISO 8601 格式、UTC 时区（如 2026-08-07T12:34:56+00:00）。 |
| `thumbnail_url` | 缩略图链接，分辨率低于 image_url。 |
| `author_follower_count` | 作者粉丝数。 |
| `search_rank` | 在这次搜索结果里的名次，从 1 开始。 |
| `platform` | 数据来源平台标识，与请求里的 platform 一致（如 xiaohongshu、tiktok）。 |
| `hashtags` | 正文里的话题标签数组，按出现顺序；没有时不出现这个字段。 |

完整参数和字段：<https://everyinfra.com/youtube-api/user_posts?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### 常见问题

**调用时要不要提供 YouTube 账号或 Cookie？**

不用，请求头带 `Authorization: Bearer` 和 API Key 就能调，请求体写 `platform`、`action` 和能力参数。不用扫码、维护登录状态，也不用开浏览器。

**怎么收费？失败了收不收钱？有免费额度吗？**

按调用次数计费，每千次 $0.56 起。失败、空结果、参数错误和鉴权失败都不收费。新账号有 $1 试用额度，24 小时内有效，不用信用卡，领取方式见定价页 <https://everyinfra.com/pricing?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

**能把 YouTube 接口接进 Claude、Cursor 吗？**

能，远程 MCP 地址是 <https://api.everyinfra.com/mcp>，请求头加 `Authorization: Bearer` 和 API Key，不用装本地程序。Claude、Cursor、ChatGPT、Claude Code 配置见 <https://everyinfra.com/mcp-server?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>。Agent 能自己搜 YouTube 内容、读评论、查账号。

**用 YouTube 数据要注意哪些合规问题？**

EveryInfra 服务条款要求你自行确保数据用法符合适用法律和相关平台条款，禁止用于违法、侵犯隐私或知识产权，或批量抓取用于骚扰、欺诈等恶意用途。用到昵称、头像等个人信息时，只留业务用得上的字段。

**可以拿到 YouTube 的哪些数据？**

YouTube 有 21 个能力：关键词搜索、主页或对象详情、用户内容、视频详情、评论、粉丝数量、视频文稿、Shorts 短视频、评论回复、相关推荐作品、频道链接和编号互查、频道帖子、频道帖子详情、频道帖子评论、频道内搜索、Shorts 关键词搜索、账号搜索、搜索联想词、视频格式信息、作品下载链接、单个格式的播放地址。每个能力的参数和返回字段见平台页 <https://everyinfra.com/youtube-api?utm_source=github&utm_medium=example_repo&utm_campaign=youtube-api>

### 实测记录

发布前用本仓的代码对线上接口跑过一遍，命令就是「快速开始」里的 5 条。

| 命令 | 时间（新加坡时间） | 返回条数 | 扣费 |
|---|---|---|---|
| `python main.py search "camping gear" --out videos.csv` | 2026-11-25 12:07 | 10 | $0.000778 |
| `python main.py video "<视频链接>" --out video.json` | 2026-11-25 12:07 | 1 | $0.000556 |
| `python main.py comments "<视频链接>" --out comments.csv` | 2026-11-25 12:07 | 20 | $0.000556 |
| `python main.py channel "<频道链接>"` | 2026-11-25 12:07 | 1 | $0.000556 |
| `python main.py videos "<频道链接>" --out channel_videos.csv` | 2026-11-25 12:08 | 10 | $0.000556 |

`video` 返回的一条（正文截到 60 字，作者字段没放进来）：

```json
{
  "id": "uWrxqBSvB3o",
  "title": "Weird New Camping Gear Everyone's Buying",
  "text": "In this video, I handed 7 pieces of outdoor gear to Jon for …",
  "like_count": 2575,
  "comment_count": 203,
  "view_count": 205141,
  "duration": "00:20:29",
  "posted_at": "2026-01-31T16:01:27+00:00"
}
```

## License

MIT
