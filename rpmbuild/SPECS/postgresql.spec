Name:           postgresql

Version:        12.9

Release:        1%{?dist}

Summary:        PostgreSQL 12.9 database server (custom compiled)

License:        PostgreSQL

URL:            https://www.postgresql.org/

Source0:        postgresql-12.9.tar.gz

BuildRequires:  gcc,readline,readline-devel,zlib,zlib-devel


%description
PostgreSQL is a powerful, open source object-relational database system.

%prep
%setup -q -n postgresql-12.9

%build
./configure --prefix=/usr/local/postgresql

make -j$(nproc)

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%files
/usr/local/postgresql

%changelog
* Thu May 15 2025 YourName <you@example.com> - 12.9-1
- Custom built PostgreSQL 12.9
