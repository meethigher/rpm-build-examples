Name:           protobuf-c

Version:        1.4.1

Release:        1%{?dist}

Summary:        protobuf-c-1.4.1.tar.gz (custom compiled)

License:        GPL-2.0

URL:            http://example.com

Source0:        protobuf-c-1.4.1.tar.gz

BuildRequires:  gcc,gcc-c++,protobuf


%description
PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.

%prep
%setup -q -n protobuf-c-1.4.1

%build
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
./configure

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=%{buildroot}

%files
/usr/local

%changelog
* Fri May 16 2025 root
- Custom built from protobuf-c-1.4.1.tar.gz