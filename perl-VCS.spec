#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
Summary:	VCS - library for generic Version Control System access in Perl
Summary(pl):	VCS - biblioteka umo¿liwiaj±ca dostêp do systemu kontroli wersji (VCS) z poziomu Perla
Name:		perl-VCS
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/VCS/VCS-%{version}.tar.gz
# Source0-md5:	5b98aa1132062ddcb455a930f85238bd
%if %{with tests}
BuildRequires:	perl-Sort-Versions
BuildRequires:	rcs
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VCS is an API for abstracting access to all version control systems
from Perl code. This is achieved in a similar fashion to the DBI suite
of modules. There are "container" classes, VCS::Dir, VCS::File, and
VCS::Version, and "implementation" classes, such as VCS::Cvs::Dir,
VCS::Cvs::File, and VCS::Cvs::Version, which are subclasses of their
respective "container" classes.

%description -l pl
VCS stanowi API dla abstrakcyjnego dostêpu z kodu w Perlu do wszelkich
systemów kontroli wersji. Osi±ga siê to w podobny sposób, jak w
zestawie modu³ów DBI. Istniej± klasy "pojemników": VCS::Dir, VCS::File
i VCS::Version oraz klasy "implementacji", takie jak: VCS::Cvs::Dir,
VCS::Cvs::File i VCS::Cvs::Version, bêd±ce podklasami swoich
odpowiednich klas "pojemników".

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
