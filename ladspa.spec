Summary:	LADSPA SDK example plugins
Name:		ladspa
Version:	1.12
Release:	1
Source0:	http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
License:	LGPL
Group:		Libraries
URL:		http://www.ladspa.org
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plugins from the LADSPA SDK.

%package devel
Summary:	Linux Audio Developer's Simple Plugin API
Group:		Libraries
Requires:	%{name} = %{version}

%description devel

There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

Definitive technical documentation on LADSPA plugins for both the host
and plugin is contained within copious comments within the ladspa.h
header file.

%prep
%setup -q -n %{name}_sdk
cd doc
#fix links to the header file in the docs
perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html


%build
cd src
%{__make} targets

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{__make} install \
    INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa \
    INSTALL_INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
    INSTALL_BINARY_DIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/COPYING
%attr(755,root,root)%{_libdir}/ladspa/*.so
%attr(755,root,root)%{_bindir}/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/COPYING
%{_includedir}/ladspa.h
