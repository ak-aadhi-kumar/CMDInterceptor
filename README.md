# CMDInterceptor
Intercepts potentially dangerous commands, and asks for confirmation.

# Instructions
1. Put `CMDInterceptor.py` to any other directory of choice.
2. Alias command in rc file as follows `alias {command}='python3 {path of CMDInterceptor.py} {command}`
3. Restart terminal

# Example
1. Extract `CMDInterceptor.py` to home directory
2. At the end of `.bashrc` put `alias rm='python3 ~/CMDInterceptor.py rm`
3. Restart terminal

