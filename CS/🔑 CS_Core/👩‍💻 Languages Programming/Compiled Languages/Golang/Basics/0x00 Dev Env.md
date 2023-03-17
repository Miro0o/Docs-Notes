# 0x00 Dev Env
[TOC]



> [Go 基础](https://www.topgoer.com)
> [Tutorial: Get started with Go](https://go.dev/doc/tutorial/getting-started)

## Getting started
![Screen Shot 2022-09-05 at 12.27.15 AM](../../../../../../Assets/Pics/Screen%20Shot%202022-09-05%20at%2012.27.15%20AM-2308842-2308845.png)
<small>A demo pic of my Golang Project</small>


### Env variables
```shell
$ go env
GO111MODULE=""
GOARCH="amd64"
GOBIN="/Users/mir0/Go/GoProjects/bin/"
GOCACHE="/Users/mir0/Go/GoCache/"
GOENV="/Users/mir0/Library/Application Support/go/env"
GOEXE=""
GOEXPERIMENT=""
GOFLAGS=""
GOHOSTARCH="amd64"
GOHOSTOS="darwin"
GOINSECURE=""
GOMODCACHE="/Users/mir0/Go/GoProjects/pkg/mod/"
GONOPROXY=""
GONOSUMDB=""
GOOS="darwin"
GOPATH="/Users/mir0/Go/GoProjects/"
GOPRIVATE=""
GOPROXY="https://proxy.golang.org,direct"
GOROOT="/usr/local/Cellar/go/1.20.1/libexec"
GOSUMDB="sum.golang.org"
GOTMPDIR=""
GOTOOLDIR="/usr/local/Cellar/go/1.20.1/libexec/pkg/tool/darwin_amd64"
GOVCS=""
GOVERSION="go1.20.1"
GCCGO="gccgo"
GOAMD64="v1"
AR="ar"
CC="clang"
CXX="clang++"
CGO_ENABLED="1"
GOMOD="/dev/null"
GOWORK=""
CGO_CFLAGS="-O2 -g"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-O2 -g"
CGO_FFLAGS="-O2 -g"
CGO_LDFLAGS="-O2 -g"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -arch x86_64 -m64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=/var/folders/vs/sbthv49974jcvdpmzgmjjqj40000gn/T/go-build367439469=/tmp/go-build -gno-record-gcc-switches -fno-common"
```
<small>My go env list</small>

- `GOBIN` : the only one go workspace's home bin
- `GOCACHE` : 
- `GOENV` : the library env of go
- `GOPATH` : the only one go workspace's home directory
- 

### Dir arch
```shell
/Users/mir0/GoProjects/
  ▾  bin/									# bin/ is used to store excutable file
       Hello *
  ▾  pkg/mod/cache/							# pkg/ is used to store cache file
       lock
  ▾  src/github.com/Mir0/test_proj_golang/	# src/ is used to store proj file
    ▾  greet/
         go.mod
         greet.go
         greet_test.go
    ▾  hello/
         go.mod
         main.go
```
<small>A demo of Go dir arch</small>

- `go.mod` tracks every module's (or package's ) own updates & other dependencies. In each module there is one `go.mod` file. Within one module every file share the same namespace in practice. 

- The `GOPATH` points to the sole workspace, under which there are `bin`, `src` and `pkg` folders, while `GOBIN` points to the sole install location of the workspace. Every proj is done under the workspace and every application is installed to the bin folder. 

- Within one module there can be a test file for every other file. Test file ends with `_test.go` and the test function in the test file begins with `TEST`


![null](../../../../../../Assets/Pics/m_314d22a4ff3892f028ce7bb6e358ef29_r.png)
<small>A more specific/vivid demonstration of GO Directory</small>


### Go run!
```go
package main  // 声明 main 包，表明当前是一个可执行程序

import "fmt"  // 导入内置 fmt 

func main(){  // main函数，是程序执行的入口
    fmt.Println("Hello World!")  // 在终端打印 Hello World!
}
```

```shell
go init
go build . 
go run .
```



## Ref
