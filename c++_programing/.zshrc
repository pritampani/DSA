# Homebrew paths
export PATH="/opt/homebrew/bin:$PATH"
export PATH="/opt/homebrew/opt/sqlite/bin:$PATH"

# SQLite flags
export LDFLAGS="-L/opt/homebrew/opt/sqlite/lib"
export CPPFLAGS="-I/opt/homebrew/opt/sqlite/include"

# MySQL paths and flags
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
export PATH="$PATH:/usr/local/mysql/bin"
export CFLAGS="-I/opt/homebrew/opt/mysql-client/include"
export LDFLAGS="-L/opt/homebrew/opt/mysql-client/lib"
