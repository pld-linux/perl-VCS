#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
Summary:	VCS perl module
Summary(pl):	Modu³ perla VCS
Name:		perl-VCS
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/VCS/VCS-%{version}.tar.gz
# Source0-md5:	0010403ee9cd69d19286a84f73e53847
%if %{with tests}
BuildRequires:	perl-Sort-Versions
BuildRequires:	rcs
%endif
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VCS - Library for generic Version Control System access in Perl.

%description -l pl
VCS - biblioteka umo¿liwiaj±ca dostêp do systemu kontroli wersji (VCS)
z poziomu perla.

%prep
%setup -q -n VCS-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/diff-hist
%{perl_vendorlib}/VCS.pm
%{perl_vendorlib}/VCS
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
