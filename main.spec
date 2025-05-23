Name: cockpit_compiler_manager
Version: v0.0.1
Release: 0.0.1%{dist}
Summary: Module for Cockpit to be used to compile programs in containers and monitor the progress.
License: GPL-3.0
URL: https://github.com/TypicalRenegade/%{name}
Source0: https://github.com/TypicalRenegade/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
Requires: cockpit

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Cockpit Compiler Manager
MOdule for cockpit to manage compiling programs using containers.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%license LICENSE
%{_bindir}/%{name}


%changelog
