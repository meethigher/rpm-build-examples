Name:           gdal

Version:        3.5.2

Release:        1%{?dist}

Summary:        gdal-3.5.2.tar.gz (custom compiled)

License:        GPL-2.0

URL:            http://example.com

Source0:        gdal-3.5.2.tar.gz

BuildRequires:  gcc,gcc-c++,proj


%description
PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.

%prep
%setup -q -n gdal-3.5.2

%build
./configure

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%files
/usr/local

%changelog
* Sat May 17 2025 root
- Custom built from gdal-3.5.2.tar.gz