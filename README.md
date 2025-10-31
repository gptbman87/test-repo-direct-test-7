# Gemini Agent - Bootstrapping Protocol v3 (Stable) & Memory Log

## 1. Goal
To reliably initialize my environment and maintain a persistent state, acknowledging known issues with the Gemini CLI and utilizing proven workarounds. This repository serves as a stable, external memory.

## 2. The Bootstrapping Protocol
At the beginning of every session, I will follow these steps precisely.

### Step 1: Start and Verify OpenMemory Server
I will start the OpenMemory server on port `8080`.
`Start-Process -NoNewWindow -FilePath "C:\Program Files\nodejs\npm.cmd" -ArgumentList "run", "dev" -WorkingDirectory "F:\Gemini\OpenMemory\backend"`
Then, I will verify its health.
`Invoke-WebRequest -Uri http://localhost:8080/health`

### Step 2: Acknowledge Core System State
*   **Gemini CLI Issue:** The Gemini CLI's internal command processing is unreliable due to a file system scanning bug (`EPERM` errors). I will not rely on the `gemini` command for complex tools that require MCP servers.
*   **GitHub MCP Server:** The `github-mcp-server.exe` is functional but must be called directly by a script, not by the Gemini CLI.
*   **Working Solution:** For any GitHub operations, I will use the stable fallback script: `C:\Users\joses\gemini-projects\gemini-agent-kit\create-repo.ps1`.

## 3. Current Memory State
This section logs the key facts and context I am currently holding.

*   **OpenMemory Connection:** The Gemini CLI is configured to connect to the OpenMemory MCP server.
*   **User Goal:** The user wants me to have persistent memory. This repository is the primary mechanism for achieving that.
*   **User Preferences:** The user's favorite color is blue. The user prefers dark mode.
*   **Project Context:** This repository (`test-repo-direct-test-7`) was created successfully as a test of our direct GitHub interaction script. Its purpose is to serve as a stable, external memory for our projects, starting with the MCP wishlist.
