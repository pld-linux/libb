Summary:	RDF triple store library
Summary(pl.UTF-8):	Biblioteka przechowywania danych RDF
Name:		libb
Version:	52393
Release:	1
License:	Apache
Group:		Applications
Source0:	http://opensource.joost.com/libb/%{name}-%{version}.tar.gz
# Source0-md5:	3e70fb8d99cac4aefe4375e8339ca31f
URL:		http://opensource.joost.com/libb/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An RDF triple store called B, a very low level C library. One of its
uses is as a backend store for redland. It's quite a bit faster than
the current backends for redland, but also still needs quite a bit of
work.

%description -l pl.UTF-8
Bardzo niskopoziomowa biblioteka C o nazwie B do przechowywania danych
RDF. Jednym z jej zastosowań jest backend przechowywania danych dla
biblioteki redland. Jest nieco szybsza niż aktualnie dostępne backendy
dla redland, ale wymaga jeszcze trochę pracy.

%package devel
Summary:	Header files for libb library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libb
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libb library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libb.

%package static
Summary:	Static libb library
Summary(pl.UTF-8):	Statyczna biblioteka libb
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libb library.

%description static -l pl.UTF-8
Statyczna biblioteka libb.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
