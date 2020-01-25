#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	WWW
%define	pnam	Google-SiteMap
Summary:	WWW::Google::SiteMap - Perl extension for managing Google SiteMaps
#Summary(pl.UTF-8):	
Name:		perl-WWW-Google-SiteMap
Version:	1.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c82bd63ca48a06374775ab7626cca974
URL:		http://search.cpan.org/dist/WWW-Google-SiteMap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Twig
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Sitemap Protocol allows you to inform search engine crawlers about URLs
on your Web sites that are available for crawling. A Sitemap consists of a
list of URLs and may also contain additional information about those URLs,
such as when they were last modified, how frequently they change, etc.

This module allows you to create and modify sitemaps.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/Google/*.pm
%{perl_vendorlib}/WWW/Google/SiteMap
%{_mandir}/man3/*
