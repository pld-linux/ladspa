Summary:	LADSPA SDK example plugins
Summary(pl):	Przyk³adowe wtyczki z LADSPA SDK
Name:		ladspa
Version:	1.12
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
# Source0-md5: dbd63dd701d80b152943073c84565c14
Patch0:		%{name}-mkdirhier.patch
URL:		http://www.ladspa.org/
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plugins from the LADSPA SDK.

%description -l pl
Istnieje wiele pakietów do syntezy u¿ywanych lub rozwijanych na
platformie linuksowej. LADSPA (Linux Audio Developer's Simple Plugin
API - proste API wtyczek dla programistów d¼wiêku pod Linuksem) to
próba udostêpnienia programistom mo¿liwo¶ci pisania prostych "wtyczek"
procesorów d¼wiêku w C/C++ i linkowania ich dynamicznie z wieloma
aplikacjami.

Ten pakiet zawiera przyk³adowe wtyczki z LADSPA SDK.

%package devel
Summary:	Linux Audio Developer's Simple Plugin API
Summary(pl):	Pakiet programistyczny LADSPA (Linux Audio Developer's Simple Plugin API)
Group:		Development/Libraries
# doesn't require base

%description devel
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

Definitive technical documentation on LADSPA plugins for both the host
and plugin is contained within copious comments within the ladspa.h
header file.

%description devel -l pl
Istnieje wiele pakietów do syntezy u¿ywanych lub rozwijanych na
platformie linuksowej. LADSPA (Linux Audio Developer's Simple Plugin
API - proste API wtyczek dla programistów d¼wiêku pod Linuksem) to
próba udostêpnienia programistom mo¿liwo¶ci pisania prostych "wtyczek"
procesorów d¼wiêku w C/C++ i linkowania ich dynamicznie z wieloma
aplikacjami.

Techniczna dokumentacja do wtyczek LADSPA dotycz±ca zarówno samych
wtyczek jak i korzystania z nich w programach znajduje siê w
komentarzach pliku nag³ówkowego ladspa.h.

%prep
%setup -q -n %{name}_sdk
%patch0 -p1
cd doc
#fix links to the header file in the docs
perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html

%build
%{__make} -C src targets \
	CC="%{__cc}" CPP="%{__cxx}" \
	CFLAGS="-I. -Wall -Werror %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	MKDIRHIER=/usr/lib/rpm/mkinstalldirs \
	INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa \
	INSTALL_INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_BINARY_DIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/ladspa/*.so

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%{_includedir}/ladspa.h
