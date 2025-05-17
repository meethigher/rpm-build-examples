Name:           postgis

Version:        3.3.2

Release:        1%{?dist}

Summary:        postgis-3.3.2.tar.gz (custom compiled)

License:        GPL-2.0

URL:            https://postgis.net/

Source0:        postgis-3.3.2.tar.gz

BuildRequires:  gcc,gcc-c++,sqlite,sqlite-devel,libxml2,libxml2-devel,postgresql,geos,proj,protobuf,protobuf-c,gdal


%description
PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.

%prep
%setup -q -n postgis-3.3.2

%build
echo -e "/usr/local/lib">/etc/ld.so.conf.d/locallib.conf
sudo ldconfig
./configure --with-pgconfig=/usr/local/postgresql/bin/pg_config

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%files
/usr/local

%changelog
* Fri May 16 2025 root
- Custom built from postgis-3.3.2.tar.gz