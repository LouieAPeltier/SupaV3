# ListRank Monorepo Setup

This is the first-pass scaffold for a list ranking product:

- **Backend:** Python + FastAPI API for list creation, public feed, and voting.
- **Frontend:** Svelte app with bright orange branding and optional Panda CSS workflow.
- **Platform target:** Google Cloud + Firebase Auth/Storage.

## Structure

- `backend/` FastAPI API + Firebase admin bootstrap.
- `frontend/` Svelte client + Firebase web SDK bootstrap + optional Panda config.

## Working with Codex + virtual dev environments

In restricted container/proxy environments, scoped npm packages can be blocked (HTTP 403).
This repo is set up so frontend bootstrapping does not require Panda by default.

To enable Panda later in an unrestricted environment:

1. `npm --prefix frontend install -D @pandacss/dev`
2. `npm --prefix frontend run panda:codegen`

## Next iteration ideas

1. Replace in-memory store with Firestore.
2. Validate Firebase ID tokens in backend middleware.
3. Add authenticated list ownership and moderation.
4. Build Panda recipes once package access is confirmed.
