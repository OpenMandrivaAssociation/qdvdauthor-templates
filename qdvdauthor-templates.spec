Name:		qdvdauthor-templates
Version:	1.11.1
Release:	%mkrel 1
Summary:	Optional menu templates for use with qdvdauthor
License:	CC-BY-SA
Group:		Video
Url:		http://qdvdauthor.sourceforge.net/
# Source0 extracted from the rpm available upstream, purged of duplicates with
# the qdvdauthor package (plugins and silence.mp2), some filename encoding 
# having been converted to utf8 using convmv -f latin1 -t utf8 --notest (buttons/Gel gruen/*) and recompressed using xz
# http://downloads.sourceforge.net/qdvdauthor/qdvdauthor-templates-1.11.1-1.i586.rpm
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Requires:	qdvdauthor

%description
This package contains optional menu templates for use with qdvdauthor.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/qdvdauthor

for d in animated buttons masks slideshow static transition 
do
  cp -R $d %{buildroot}%{_datadir}/qdvdauthor
done

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc COPYING
%{_datadir}/qdvdauthor/*
