%define upstream_name    CPAN-Meta-Check
%define upstream_version 0.004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Verify requirements in a CPAN::Meta object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPAN::Meta) >= 2.120.920
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.120.920
BuildRequires:	perl(Exporter) >= 5.570.0
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.300.0
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Metadata)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::More) >= 0.880.0
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildArch:	noarch

%description
This module verifies if requirements described in a CPAN::Meta object are
present.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes INSTALL LICENSE META.json META.yml MYMETA.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

