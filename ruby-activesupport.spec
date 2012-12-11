%define	rname	activesupport

Summary:	Support and utility classes used by the Rails framework
Name:		ruby-%{rname}
Version:	3.2.3
Release:	2
URL:		http://as.rubyonrails.com/
Source0:	http://rubygems.org/downloads/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 
Provides:	rubygem(%{rname})
Provides:	rubygem-activesupport

%description
Utility library which carries commonly used classes and goodies from the Rails
framework.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --no-rdoc --no-ri --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec


%changelog
* Tue Apr 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.2.3-2
+ Revision: 791467
- provides: rubygem-activesupport
- broken BR dep removed

* Thu Apr 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.2.3-1
+ Revision: 789360
- fix broken name
- version update 3.2.3

* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.1-2
+ Revision: 773441
- rebuild for ruby 1.9

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 3.2.1-1
+ Revision: 769694
- New release

* Tue Sep 27 2011 Alexander Barakin <abarakin@mandriva.org> 3.1.0-1
+ Revision: 701457
- imported package ruby-activesupport

* Tue Mar 15 2011 Rémy Clouard <shikamaru@mandriva.org> 2.3.11-1
+ Revision: 645166
- new version 2.3.11

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix url

* Thu Dec 09 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-2mdv2011.0
+ Revision: 618305
- add provides to fix rails dependencies

* Fri Oct 15 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-1mdv2011.0
+ Revision: 585825
- bump release

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.9-1mdv2011.0
+ Revision: 579503
- new release: 2.3.9

* Sun Sep 13 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.4-1mdv2011.0
+ Revision: 438619
- Update to new version 2.3.4

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.3-1mdv2010.0
+ Revision: 402805
- Update to new version 2.3.3

* Fri Jun 12 2009 Lev Givon <lev@mandriva.org> 2.1.2-1mdv2010.0
+ Revision: 385322
- Update to 2.1.2.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-2mdv2009.0
+ Revision: 269230
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.1.0-1mdv2009.0
+ Revision: 214636
- new version 2.1.0

* Mon Jan 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 151202
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Olivier Blin <blino@mandriva.org> 1.4.2-1mdv2008.0
+ Revision: 17549
- 1.4.2

  + Pascal Terjan <pterjan@mandriva.org>
    - ri is now in ri/ and not ri/ri/
    - Use Development/Ruby group

