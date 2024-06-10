## Ollama로 개인비서를 만들어 봅시다

여기서는 윈도우환경에서 설명드리겠습니다.

# 단계1

Ollama는 공식 웹사이트에서 다운로드 받을 수 있습니다. (https://www.ollama.com/)

다운로드를 받은 설치파일(OllamaSetup.exe, 약 210MB)을 실행합니다.

설치 후, ollama는 쉘 환경에서 실행합니다.

(예: cmd, powershell, zsh)

설치가 되면 다음과 같이 

```cmd
C:<경로>> ollama

Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information

Use "ollama [command] --help" for more information about a command.
```

위와 같이 출력이 되면 설치가 완료가 된 것입니다.

