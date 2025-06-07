Name:           python3

Version:        3.11.12

Release:        1%{?dist}

Summary:        Python-3.11.12.tar.gz (custom compiled)

License:        GPL-2.0

URL:            http://example.com

Source0:        Python-3.11.12.tar.gz

BuildRequires:  gcc,zlib,zlib-devel


# 问题1
# Python编译rpm中的坑较多，有很多已经deprecated的代码，但是仍然保留了下来，这对于不同的操作系统编译rpm时，就会遇到各种各样问题。
# 在将python编译为rpm后，进行安装时，遇到问题/usr/local/bin/python is needed by python3-3.11.12-1.el9.aarch64
# grep -r '^#!.*python' Python-3.11.12/|grep /usr/local/bin/python
# 定位到是因为Python-3.11.12/Lib/cgi.py，需要手动调整源码，将/usr/local/bin/python修改为/usr/bin/env python3，然后重新打包

# 问题2
# rpm打包系统中的brp-mangle-shebangs在处理shebang（#!/usr/bin/env python）时，使用的版本模糊不清，就会编译rpm失败。这是rpm打包系统的规范。
# 而python中为了兼容旧版，是保留了这些旧代码的。在编译rpm时，可选解决办法有两种，一是自己手动修改Python源码，二是加入下面这行代码
%global __brp_mangle_shebangs %{nil}

# 问题3
# rpm打包时，在make && make install之后，还会进行一些语法检查。这在直接编译安装时，是不需要的。
# 针对python的rpm打包，若有旧版python环境，则会使用旧版python验证*.py语法，就会出现SyntaxError: invalid syntax
# 参考https://stackoverflow.com/questions/69053126/syntaxerror-invalid-syntax-error-when-building-python-3-8-9-source-code-as-a
# 可选解决办法有两种，一是拿掉旧版python，二是加入下面这行代码（让/usr/lib/rpm/brp-python-bytecompile不检查语法）
%global __brp_python_bytecompile %{nil}

%description
Python 3.11.12

%prep
%setup -q -n Python-3.11.12

%build
./configure --prefix=/usr/local/python-3.11.12

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%files
/usr/local/python-3.11.12

%changelog
* Thu Jun 5 2025 root
- Custom built from Python-3.11.12.tar.gz