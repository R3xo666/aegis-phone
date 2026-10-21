#!/usr/bin/env bash
# ==============================================================================
# Aegis-Phone Universal Installer & Environment Setup
# Installs dependencies, sets permissions, and creates global symlink on Linux
# ==============================================================================

set -eo pipefail

INSTALL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_TARGET="${HOME}/.local/bin"

echo "🚀 Setting up Aegis-Phone on your system..."

# 1. Ensure ~/.local/bin exists and is in user PATH
mkdir -p "$BIN_TARGET"

# 2. Grant execution permissions
chmod +x "${INSTALL_DIR}/phone"
chmod +x "${INSTALL_DIR}/phone_deck.py"
[ -f "${INSTALL_DIR}/adb" ] && chmod +x "${INSTALL_DIR}/adb"
[ -f "${INSTALL_DIR}/scrcpy" ] && chmod +x "${INSTALL_DIR}/scrcpy"

# 3. Create global symlink
ln -sf "${INSTALL_DIR}/phone" "${BIN_TARGET}/phone"

echo "✔ Global symlink created: ${BIN_TARGET}/phone -> ${INSTALL_DIR}/phone"

# 4. PATH check
if [[ ":$PATH:" != *":$BIN_TARGET:"* ]]; then
    echo "ℹ Adding ~/.local/bin to your shell environment..."
    SHELL_RC="$HOME/.bashrc"
    [ -n "$ZSH_VERSION" ] && SHELL_RC="$HOME/.zshrc"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
    echo "✔ Updated $SHELL_RC. Run 'source $SHELL_RC' or restart your terminal."
fi

echo -e "\n🎉 Installation Complete!"
echo "Run 'phone status' or 'phone --help' to get started."
