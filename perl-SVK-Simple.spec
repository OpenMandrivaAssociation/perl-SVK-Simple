%define upstream_name    SVK-Simple
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simple interface to svk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/G/GU/GUGOD/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Class::Field)
BuildRequires:  perl(SVK)
BuildRequires:  perl(Spiffy)
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Although SVK.pm itself is already simple enough, there still are some misc 
requirements in the svk script which is not included in SVK.pm. This module 
helps people who wants to write some SVK applications. It provides a simple 
SVK object loader, so people will not have to handle XD initialization.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README 
%{perl_vendorlib}/*
%{_mandir}/man3/*
