#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# Requires configured MySQL local database

%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	TextIndex
Summary:	DBIx::TextIndex - Perl extension for full-text searching in SQL databases
Summary(pl):	DBIx::TextIndex - rozszerzenie do pe³notekstowego przeszukiwania baz SQL
Name:		perl-DBIx-TextIndex
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af19205380c2d845f0cb095ac93c7300
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Bit-Vector
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl-Exception-Class
#BuildRequires:	perl-Text-Unaccent # Not in PLD yet
BuildRequires:	perl(Text::Balanced) # core perl module since 5.8
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::TextIndex was developed for doing full-text searches on BLOB
columns stored in a database. Almost any database with BLOB and DBI
support should work with minor adjustments to SQL statements in the
module.

%description -l pl
Modu³ DBIx::TextIndex s³u¿y do przeprowadzania pe³notekstowych
przeszukiwañ kolumn BLOB zapisanych w bazie danych. Prawie ka¿da baza
danych z obs³ug± BLOB i DBI powinna dzia³aæ po niewielkich poprawkach
wyra¿eñ SQL w module.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf eg/README
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%{perl_vendorarch}/%{pdir}/%{pnam}
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
