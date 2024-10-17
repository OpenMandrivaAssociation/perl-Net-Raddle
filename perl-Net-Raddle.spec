%define debug_package %{nil}

%define upstream_name Net-Raddle

Name:		perl-%{upstream_name}
Version:	0.08
Release:	5
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Raddle network emulator
Url:		https://raddle.sourceforge.net/
Source:		http://downloads.sourceforge.net/project/raddle/raddle/%{version}/Net-Raddle-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(NetSNMP::ASN)
BuildRequires:	perl(Date::Calc)

%description
Raddle is a network emulation framework. It is particularly useful when testing
network management systems or teaching people to use them.

%prep
%setup -q -n %{upstream_name}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGELOG INSTALLATION LICENCE README examples
%{_mandir}/man3/*
%{perl_vendorlib}/*
