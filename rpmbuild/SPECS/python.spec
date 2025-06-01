Name:           python3

Version:        3.11.12

Release:        1%{?dist}

Summary:        Python-3.11.12.tar.gz (custom compiled)

License:        GPL-2.0

URL:            http://example.com

Source0:        Python-3.11.12.tar.gz

BuildRequires:  gcc,zlib,zlib-devel


# 说明
# Python编译rpm中的坑较多，有很多已经deprecated的代码，但是仍然保留了下来，这对于不同的操作系统编译rpm时，就会遇到各种各样问题。
# 在将python编译为rpm时，遇到个问题/usr/local/bin/python is needed by python3-3.11.12-1.el9.aarch64
# grep -r '^#!.*python' Python-3.11.12/|grep /usr/local/bin/python
# 定位到是因为Python-3.11.12/Lib/cgi.py，需要手动修改一下源码，然后重新打包

# rpm打包系统中的brp-mangle-shebangs在处理shebang（#!/usr/bin/env python）时，如果使用的版本模糊不清，就会编译rpm失败。
# 而python中为了兼容旧版，是保留了这些旧代码的，因此编译时，需要禁用掉系统检查，或者自己手动修改Python源码
%global __brp_mangle_shebangs %{nil}

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