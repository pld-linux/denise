#
# now project are suspended
Summary:	Denise(R)-MYTH Artificial Intelligence
Summary(pl):	Denise(R)-MYTH Sztuczna Inteligencja
Name:		denise
Version:	5.1.1
Release:	1
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://denise.union.pl/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	2d2f01a0ef379424d29ee0ad1975310a
Patch0:		%{name}-freemem.patch
URL:		http://www.denise.union.pl/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Denise(R)-MYTH project is a very interesting attemption of create
artificial intelligence.

%description -l pl
Projekt Denise(R)-MYTH jest interesuj�c� pr�b� podj�cia tematu
sztuczniej inteligencji.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}

%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/denise
%{_datadir}/denise
