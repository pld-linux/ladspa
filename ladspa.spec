Summary:	LADSPA SDK example plugins
Summary(pl.UTF-8):	Przykładowe wtyczki z LADSPA SDK
Name:		ladspa
Version:	1.13
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
# Source0-md5:	671be3e1021d0722cadc7fb27054628e
Patch0:		%{name}-mkdirhier.patch
Patch1:		%{name}-gcc4.patch
URL:		http://www.ladspa.org/
BuildRequires:	perl-base
BuildRequires:	libstdc++-devel
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plugins from the LADSPA SDK.

%description -l pl.UTF-8
Istnieje wiele pakietów do syntezy używanych lub rozwijanych na
platformie linuksowej. LADSPA (Linux Audio Developer's Simple Plugin
API - proste API wtyczek dla programistów dźwięku pod Linuksem) to
próba udostępnienia programistom możliwości pisania prostych "wtyczek"
procesorów dźwięku w C/C++ i ich dynamicznej konsolidacji z wieloma
aplikacjami.

Ten pakiet zawiera przykładowe wtyczki z LADSPA SDK.

%package common
Summary:	Common environment for LADSPA plugins
Summary(pl.UTF-8):	Środowisko wspólne dla wtyczek LADSPA
Group:		Libraries

%description common
Common environment for LADSPA plugins. Currently it contains only
appropriate directory trees.

%description common -l pl.UTF-8
Środowisko wspólne dla wtyczek LADSPA. Aktualnie zawiera tylko
odpowiednie drzewa katalogów.

%package devel
Summary:	Linux Audio Developer's Simple Plugin API
Summary(pl.UTF-8):	Pakiet programistyczny LADSPA (Linux Audio Developer's Simple Plugin API)
Group:		Development/Libraries
# doesn't require base or common

%description devel
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

Definitive technical documentation on LADSPA plugins for both the host
and plugin is contained within copious comments within the ladspa.h
header file.

%description devel -l pl.UTF-8
Istnieje wiele pakietów do syntezy używanych lub rozwijanych na
platformie linuksowej. LADSPA (Linux Audio Developer's Simple Plugin
API - proste API wtyczek dla programistów dźwięku pod Linuksem) to
próba udostępnienia programistom możliwości pisania prostych "wtyczek"
procesorów dźwięku w C/C++ i ich dynamicznej konsolidacji z wieloma
aplikacjami.

Techniczna dokumentacja do wtyczek LADSPA dotycząca zarówno samych
wtyczek jak i korzystania z nich w programach znajduje się w
komentarzach pliku nagłówkowego ladspa.h.

%prep
%setup -q -n %{name}_sdk
%patch0 -p1
%patch1 -p1
cd doc
#fix links to the header file in the docs
perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html

%build
%{__make} -C src targets \
	CC="%{__cc}" CPP="%{__cxx}" \
	CFLAGS="-I. -Wall -Werror %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf

%{__make} -C src install \
	MKDIRHIER="/usr/bin/install -d" \
	INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa \
	INSTALL_INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_BINARY_DIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/ladspa/*.so

%files common
%defattr(644,root,root,755)
%dir %{_libdir}/ladspa
%dir %{_datadir}/ladspa
%dir %{_datadir}/ladspa/rdf

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%{_includedir}/ladspa.h
