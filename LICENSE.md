The MIT License (MIT)

Original work Copyright (c) 2015 [Far End Technologies Corporation](http://www.farend.co.jp/)

Modified work Copyright (c) 2024 H.Matsutani -- staff of [Redmine.tokyo](https://redmine.tokyo/)/[Redmine Japan](https://redmine-japan.org/) 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Modifications:
- Changed from CentOS to Rocky Linux 8.9 as the OS
- Modified to obtain Redmine/RedMica from the git repository
- Install Ruby using rbenv
- Create Swap if swap is 0
- For RedMica 3.0.0, install Farend_basic (propshaft version)
- Not for RedMica 3.0.0, install the Farend_basic theme (master version)
- Create a Gemfile.local to avoid installing the builder(3.0.0) gem
- Added Remove task for uninstall Redmine
