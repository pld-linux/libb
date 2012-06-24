#
Summary:	RDF triple store library
Summary(pl.UTF-8):	-
Name:		libb
Version:	52393
Release:	1
License:	Apache
Group:		Applications
Source0:	http://opensource.joost.com/libb/libb-52393.tar.gz
# Source0-md5:	3e70fb8d99cac4aefe4375e8339ca31f
#Patch0:		%{name}-DESTDIR.patch
URL:		http://opensource.joost.com/libb/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An RDF triple store called B, a very low level C library. One of its uses is
as a backend store for redland. It's quite a bit faster than the current
backends for redland, but also still needs quite a bit of work.

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
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
