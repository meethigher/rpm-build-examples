Name:           geos

Version:        3.9.4

Release:        1%{?dist}

Summary:        geos-3.9.4.tar.gz (custom compiled)

License:        GPL-2.0

URL:            http://example.com

Source0:        geos-3.9.4.tar.gz

BuildRequires:  gcc,gcc-c++


%description
PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.

%prep
%setup -q -n geos-3.9.4

%build
./configure

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%files
/usr/local

%changelog
* Fri May 16 2025 root
- Custom built from geos-3.9.4.tar.gz