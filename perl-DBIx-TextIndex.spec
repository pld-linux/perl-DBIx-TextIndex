#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	TextIndex
Summary:	DBIx::TextIndex - Perl extension for full-text searching in SQL databases
Summary(pl):	DBIx::TextIndex - rozszerzenie do pe³notekstowego przeszukiwania baz SQL
Name:		perl-DBIx-TextIndex
Version:	0.11
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl(Data::Dumper)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::TextIndex was developed for doing full-text searches on BLOB
columns stored in a database. Almost any database with BLOB and DBI
support should work with minor adjustments to SQL statements in the
module.

%description -l pl
Modu³ DBIx::TextIndex s³u¿y do przeprowadzania pe³notekstowych
przeszukiwañ kolumn BLOB zapisanyc w bazie danych. Prawie ka¿da baza
danych z obs³ug± BLOB i DBI powinna dzia³aæ po niewielkich poprawkach
wyra¿eñ SQL w module.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf examples/{README,*.txt}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
