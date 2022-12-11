<p align=center>
<img src="https://github.com/misaraty/juliaplus/blob/master/logo.jpg" width=300px height=auto/>
</p>

**Julia+** is a project that provides the installation of third-party scientific computing packages.

Julia v1.8.2 with [CarrierCapture.jl](https://github.com/WMD-group/CarrierCapture.jl), [PyCall.jl](https://github.com/JuliaPy/PyCall.jl) packages, and will be continuously updated.

Runtime environment: Centos 7+, Windows 7/8/10/11.

## Preparations before installation

### Centos 7+

* Download [Julia v1.8.2 64-bit (.tar.gz)](https://julialang.org/downloads/), then,

```bash
tar -zxvf julia-1.8.2-linux-x86_64.tar.gz
```

* Modify `.bashrc` or `.bash_profile`,

```bash
# julia
export PATH=$PATH:/home/misaraty/soft/julia-1.8.2/bin
export JULIA_PKG_SERVER=https://mirrors.bfsu.edu.cn/julia
# export JULIA_DEPOT_PATH="/home/misaraty/soft/julia-1.8.2/.julia"
```

* Accelerate git,

```bash
mk ~/.git
git config --global url."https://ghproxy.com/https://github.com/".insteadOf "https://github.com/"
git config protocol.https.allow always
```

### Windows 7/8/10

* Download [Julia v1.8.2 64-bit (portable)](https://julialang.org/downloads/) and [scripts](https://github.com/misaraty/juliaplus/tree/master/windows).

* Put the scripts into the Julia decompression path, and run `add_path.bat` or `delete_path.bat` as an administrator to add or delete environment variables, respectively.

Warning: The scripts are not suitable for Windows11, because they will report an error `The data being saved is truncated to 1024 characters`.

* Modify `C:\Users\lenovo\AppData\Local\Programs\Julia-1.8.2\etc\julia\startup.jl`, 

```bash
ENV["HTTP_PROXY"] = "socks5://127.0.0.1:7890"
ENV["HTTPS_PROXY"] = "socks5://127.0.0.1:7890"
```

### Windows 11

* Download [Julia v1.8.2 64-bit (installer)](https://julialang.org/downloads/).

* Modify `C:\Users\lenovo\AppData\Local\Programs\Julia-1.8.2\etc\julia\startup.jl`, 

```bash
ENV["HTTP_PROXY"] = "socks5://127.0.0.1:7890"
ENV["HTTPS_PROXY"] = "socks5://127.0.0.1:7890"
```

## Third-party package installation

* [CarrierCapture.jl](https://github.com/WMD-group/CarrierCapture.jl)

```bash
using Pkg; Pkg.add(PackageSpec(url="https://github.com/WMD-group/CarrierCapture.jl"))
Pkg.add("Plots"); Pkg.add("LaTeXStrings");Pkg.add("DataFrames")
# import Pkg; Pkg.precompile()
using CarrierCapture
```

* [PyCall.jl](https://github.com/JuliaPy/PyCall.jl)

```bash
using Pkg; Pkg.add("PyCall")
ENV["PYTHON"]="C:/Users/lenovo/anaconda3/python.exe"
Pkg.build("PyCall")
using PyCall
```

## Contact

website: https://www.misaraty.com

email: misaraty@163.com

## Acknowledgement

Thanks to Julia and the third-party packages developers.

