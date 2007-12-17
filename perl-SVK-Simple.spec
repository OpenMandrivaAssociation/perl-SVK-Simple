%define realname   SVK-Simple

Name:		perl-%{realname}
Version:        0.02
Release:        %mkrel 7
License:	GPL or Artistic
Group:		Development/Perl
Summary:        This module is a simple interface to svk
Source0:        http://search.cpan.org/CPAN/authors/id/G/GU/GUGOD/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl-Spiffy
BuildRequires:  perl-SVK
BuildArch:      noarch

%description
Although SVK.pm itself is already simple enough, there still are some misc 
requirements in the svk script which is not included in SVK.pm. This module 
helps people who wants to write some SVK applications. It provides a simple 
SVK object loader, so people will not have to handle XD initialization.

%prep
%setup -q -n %{realname}-%{version}

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
