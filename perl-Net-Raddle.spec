%define upstream_name Net-Raddle
%define version    0.08
%define release    %mkrel 1

Name:       perl-%{upstream_name}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Raddle network emulator
Url:        http://raddle.sourceforge.net/
Source:     http://downloads.sourceforge.net/project/raddle/raddle/%{version}/Net-Raddle-%{version}.tar.gz
BuildRequires: perl(Test::More)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Raddle is a network emulation framework. It is particularly useful when testing network management systems or teaching people to use them.

%prep
%setup -q -n %{upstream_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG INSTALLATION LICENCE README examples
%{_mandir}/man3/*
%perl_vendorlib/*

