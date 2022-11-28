# 0x00 Bsics

> [Go 基础](https://www.topgoer.com)
>
> [Tutorial: Get started with Go](https://go.dev/doc/tutorial/getting-started)



## Getting started



![Screen Shot 2022-09-05 at 12.27.15 AM](../../../../../Assets/Pics/Screen Shot 2022-09-05 at 12.27.15 AM-2308842-2308845.png)

<small>A demo pic of my Golang Project</small>



### Env variables

```shell
GOPATH="/Users/mir0/GoProjects/"
GOPRIVATE=""
GOPROXY="https://proxy.golang.org,direct"
GOROOT="/usr/local/Cellar/go/1.19.2/libexec"
GOSUMDB="sum.golang.org"
GOTMPDIR=""
GOTOOLDIR="/usr/local/Cellar/go/1.19.2/libexec/pkg/tool/darwin_amd64"
GOVCS=""
GOVERSION="go1.19.2"
GCCGO="gccgo"
GOAMD64="v1"
AR="ar"
CC="clang"
CXX="clang++"
CGO_ENABLED="1"
GOMOD="/dev/null"
GOWORK=""
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -arch x86_64 -m64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=/var/folders/vs/sbthv49974jcvdpmzgmjjqj40000gn/T/go-build3808678275=/tmp/go-build -gno-record-gcc-switches -fno-common"
```

<small>My go env list</small>





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



- `go.mod` tracks every module's (or package's ) own updates & other dependencies . In each module there is one `go.mod` file. Within one module every file share the same namespace in practice. 

- The `GOPATH` points to the sole workspace, under which there are `bin`, `src` and `pkg` folders, while `GOBIN` points to the sole install location of the workspace. Every proj is done under the workspace and every application is installed to the bin folder. 

- Within one module there can be a test file for every other file. Test file ends with `_test.go` and the test  function in the test file begins with `TEST`



![null](../../../../../Assets/Pics/m_314d22a4ff3892f028ce7bb6e358ef29_r.png)

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





## Basic Syntex 

> [Go 基础](https://www.topgoer.cn/docs/golang/chapter02-1)



```shell
# Go key words:
	break        default      func         interface    select
    case         defer        go           map          struct
    chan         else         goto         package      switch
    const        fallthrough  if           range        type
    continue     for          import       return       var
    
# Go reserved words:
Constants:    true  false  iota  nil

Types:    int  int8  int16  int32  int64  
          uint  uint8  uint16  uint32  uint64  uintptr
          float32  float64  complex128  complex64
          bool  byte  rune  string  error

Functions:   make  len  cap  new  append  copy  close  delete
             complex  real  imag
             panic  recover
             
# Go Value type:
    bool
    int(32 or 64), int8, int16, int32, int64
    uint(32 or 64), uint8(byte), uint16, uint32, uint64
    float32, float64
    string
    complex64, complex128
    array    -- 固定长度的数组

# Go referance type:
    slice   -- 序列数组(最常用)
    map     -- 映射
    chan    -- 管道
    

```

