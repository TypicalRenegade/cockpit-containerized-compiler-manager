Name: cockpit_compiler_manager
Version: v0.0.1
Release: 0.0.1%{dist}
Summary: Module for Cockpit to be used to compile programs in containers and monitor the progress.
License: MIT
URL: https://github.com/TypicalRenegade/cockpit-containerized-compiler-manager
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: cockpit

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Cockpit Compiler Manager
MOdule for cockpit to manage compiling programs using containers.

%prep
%setup -q

%build
make OS_PACKAGE_RELEASE=el8

%install
make DESTDIR=%{buildroot} install

%files
/usr/share/cockpit/compiler_manager/*

%changelog
