Name: ::package_name::
Version: ::package_version::
Release: ::package_build_version::%{dist}
Summary: ::package_description_short::
License: ::package_licence::
URL: ::package_url::
Source0: %{name}-%{version}.tar.gz
BuildArch: ::package_architecture_el::
Requires: ::package_dependencies_el_generic::

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
::package_title::
::package_description_long::

%prep
%setup -q

%build
make OS_PACKAGE_RELEASE=el8

%install
make DESTDIR=%{buildroot} install

%files
/usr/share/cockpit/compiler_manager/*

%changelog
