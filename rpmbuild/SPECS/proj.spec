Name:           proj

Version:        6.3.2

Release:        1%{?dist}

Summary:        proj-6.3.2.tar.gz (custom compiled)

License:        GPL-2.0

URL:            http://example.com

Source0:        proj-6.3.2.tar.gz

BuildRequires:  gcc,gcc-c++,sqlite,sqlite-devel


%description
PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.

%prep
%setup -q -n proj-6.3.2

%build
./configure

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%files
/usr/local

%changelog
* Fri May 16 2025 root
- Custom built from proj-6.3.2.tar.gz
