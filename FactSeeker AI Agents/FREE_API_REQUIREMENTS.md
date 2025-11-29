# Free Tier API Requirements for FactSeeker

## Summary
All services listed below have **FREE TIERS** - no payment required!

---

## 1. HuggingFace Token (REQUIRED)
**Purpose**: Free LLM inference for fact-checking

**How to get**:
1. Go to https://huggingface.co/join
2. Sign up (free)
3. Go to https://huggingface.co/settings/tokens
4. Click "New token" → Create (Read access is enough)
5. Copy the token (starts with `hf_`)

**Free Tier**: 20,000 API requests/month
**Cost**: $0

---

## 2. NewsAPI Key (OPTIONAL)
**Purpose**: Fetch real news articles

**How to get**:
1. Go to https://newsapi.org/register
2. Sign up (free)
3. Copy your API key from dashboard

**Free Tier**: 100 requests/day
**Cost**: $0

---

## 3. Reddit API (OPTIONAL)
**Purpose**: Fetch Reddit posts

**How to get**:
1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App" or "Create Another App"
3. Select "script" type
4. Copy Client ID (under app name) and Secret

**Free Tier**: 60 requests/minute
**Cost**: $0

---

## 4. Telegram Bot Token (OPTIONAL)
**Purpose**: Send alerts via Telegram

**How to get**:
1. Open Telegram app
2. Search for @BotFather
3. Send `/newbot` command
4. Follow instructions to create bot
5. Copy the token provided

**Free Tier**: Unlimited
**Cost**: $0

---

## 5. MongoDB Atlas (OPTIONAL)
**Purpose**: Store data persistently

**How to get**:
1. Go to https://www.mongodb.com/cloud/atlas/register
2. Sign up (free)
3. Create a free cluster (M0)
4. Get connection string from "Connect" button

**Free Tier**: 512MB storage
**Cost**: $0

---

## Minimum Required
To run FactSeeker with free APIs, you only need:
- ✅ **HuggingFace Token** (for LLM)

Everything else is optional or already works locally!

---

## What to Provide
Please share any of these you want to use:
```
HUGGINGFACE_TOKEN=hf_your_token_here
NEWS_API_KEY=your_newsapi_key_here (optional)
REDDIT_CLIENT_ID=your_reddit_id (optional)
REDDIT_CLIENT_SECRET=your_reddit_secret (optional)
TELEGRAM_BOT_TOKEN=your_bot_token (optional)
MONGODB_URI=your_mongodb_uri (optional)
```
