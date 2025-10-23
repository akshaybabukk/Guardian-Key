# Guardian-Key
This tool is designed to help users assess the strength of their passwords and check whether they’ve been exposed in public data breaches using the trusted Have I Been Pwned API.
<p>💡 Features at a glance:
<ul>
  <li>Evaluates password strength based on length, character variety, and complexity.</li>
  <li>Uses SHA1 hashing and API query prefix matching to check if a password has been pwned.</li>
  <li>Displays how many times the password appears in leaked datasets.</li>
  <li>Provides actionable feedback for users to improve weak passwords instantly.</li>
</ul>
</p>
<p>
<h4>Prerequisites</h4>
<p></p>Make sure these are installed on your system before deploying:</p>
<ul>
<li>Python 3.8 or above</li>

<li>Flask (pip install flask)</li>

<li>requests library (pip install requests)</li>

<li>Regular expressions (built into Python)</li>

<li>Modern browser (Chrome/Edge/Firefox)</li>
</ul>
</p>

<h4>Run Locally</h4>
<p>Clone it in your IDE environment.</p>
<p>Navigate to the project directory in terminal:
 <p> > cd GuardianKey</p>
 <p> > py main.py</p>
 
 <p>Then open the URL displayed, usually:</p>
 
> http://127.0.0.1:5000/

<p>You’ll see the Guardian Key interface where you can test passwords and view their strength and pwned status.</p>
