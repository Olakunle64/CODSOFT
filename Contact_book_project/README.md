<h2>Contact Console</h2>
<h4>This project focuses on creating a contact book for saving contacts details and it uses
    file storage as the storage engine
</h4>
<p>Default details you might want to save includes:</p>
<ul>
    <li>name</li>
    <li>phone number</li>
    <li>address</li>
    <li>email</li>
</ul>
<p><b>Note:</b> You can save more details apart from the default details stated above</p>
<p>HOW TO START THE CONSOLE</p>
<ul>
    <li>Step 1: clone the repository and navigate to Contact_book_project directory</li>
    <li>Step 2: Type ./console.py on the terminal to start the console</li>
</ul>
<p>The following includes various operation allowed by the console</p>
<ol>
    <li>add <em>PHONE_NUMBER</em></li>
    <li>search <em>PHONE_NUMBER</em> OR search <em>NAME</em></li>
    <li>display</li>
    <li>update <em>PHONE_NUMBER  DICTIONARY_ATTRIBUTE</em></li>
    <li>delete <em>PHONE_NUMBER</em></li>
    <li>quit</li>
    <li>help</li>
</ol>
<p>Short note on the operations listed above:</p>
<ol>
    <li>add: This method allows you to add new contact details by specifying the phone number alone. <b>Note</b> that
        the phone number is a unique feature of the contact details hence, you can only save a particular phone number
        once otherwise it will raise an error that the phone number already exist!
    </li>
    <li>search: This method allows you to search for a contact either by name or by phone number. <b>Note</b> that
        the search function also performs wonders such that when you have olakunle as a name of an already existing
        contact detail and you type <b>search ola</b> on the console, it will list all contact details having ola
        in the name attribute likewise when you have 07062869135 as a phone number of an already existing contact detail
        and you type <b>search 9135</b> on the console, it will list all contact details having 9135 in the
        phone_number attribute.
    </li>
    <li>display: This method display all existing contant details in the storage engine</li>
    <li>update: This method update the contact detail having the corresponding phone number with the dictionary attribute</li>
    <li>delete: This method delete the contact detail with the corresponding phone number</li>
    <li>quit: This method quit the console</li>
    <li>help: This method shows help on how to use the console. <em>Note</em> that you can also specify you help by typing
        help with specific method you want to know more about.
    </li>
</ol>

<p>Dont forget to star the repository and follow me on github.</p>
<em>THANK YOU</em>

