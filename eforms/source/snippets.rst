
Code Snippets
=============

In this document you will find preconfigured code snippets to make it easier to create new eForms.

LogipadHeader
-------------

Header with title, logo and version.
You can change **logipad_aero.png** to the filename of your company logo in the images folder.

..

   Snippet: logipadheader


.. code-block:: xml

   <!-- START OF HEADER-->",
   <p></p>
   <div class="row">
       <div class="col-sm-9">
           <label class="control-label Title">
               ${FormName}
           </label>
       </div>
       <div class="col-sm-3">
           <div class="row">
               <div class="col-sm-12" align="right">
                   <img src="./images/logipad_aero.png" width="200px"></img>
               </div>
           </div>
           <div class="row">
               <div class="col-sm-12" align="right">
                   eForm Version 1.2
               </div>
           </div>
       </div>
   </div>
   <p></p>
   <!-- END OF HEADER-->

LogipadSection
--------------

Head and **Content** area of a new section. It can be insert a **Sectionname**.

..

   Snippet: logipadsection


.. code-block:: xml

   <!-- START Section ${Sectionname} -->
   <div class="row">
       <div class="col-sm-12">
           <div class="SectionHeader SectionTitle">
               ${Sectionname}
           </div>
           <p></p>
       </div>
   </div>
   ${Content}
   <!-- END Section ${Sectionname} -->

LogipadInput
------------

Input box with **Labeltext** and field name **Variablename**.
The width of the field can be set with **width**.

..

   Snippet: logipadinput


.. code-block:: xml

   <!-- Start LogipadInput -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="text" class="form-control" name="${Variablename}"></input>
       </div>
   </div>
   <!-- End LogipadInput -->

Input where the input is required.

..

   Snippet: logipadinputrequired


.. code-block:: xml

   <!-- Start LogipadInputRequired -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="text" class="form-control" name="${Variablename}" required="required"></input>
       </div>
   </div>
   <!-- End LogipadInputRequired -->

Input to input a three letter code.
If the logipad keyboard is activated a custom keyboard will be used.

..

   Snippet: logipadinput3lc


.. code-block:: xml

   <!-- Start LogipadInput3LC -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="three-lc" class="form-control" name="${Variablename}"></input>
       </div>
   </div>
   <!-- End LogipadInput3LC -->

Input field for input numbers with a numeric keypad.

..

   Snippet: logipadinputnumber


.. code-block:: xml

   <!-- Start LogipadInputNumber -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="number" class="form-control" name="${Variablename}"></input>
       </div>
   </div>
   <!-- End LogipadInputNumber -->

LogipadSelect
-------------

Select field whose options are filled from the backend.
With the attribute **data-live-search** the search field in the options can be activated.

..

   Snippet: logipadselect1


.. code-block:: xml

   <!-- Start LogipadSelect1 -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <select class="selectpicker form-control" name="${Variablename}" required="required" data-live-search="true" title="Select..."></select>
       </div>
   </div>
   <!-- End LogipadSelect1 -->

Select field whose options are implemented insinde the form.

..

   Snippet: logipadselect2


.. code-block:: xml

   <!-- Start LogipadSelect2 -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <select class="selectpicker form-control" name="${Variablename}" title="Select ...">
               <option value="${Option1}">${Option1}</option>
               <option value="${Option2}">${Option2}</option>
               <option value="Other">Other ...</option>
           </select>
       </div>
   </div>
   <!-- End LogipadSelect2 -->

Radio group
-----------

Button radio group with the values yes and no. The values can be changed.

..

   Snippet: logipadradio


.. code-block:: xml

   <!-- Start LogipadRadio -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <br></br>
           <div class="btn-group btn-group-toggle LogipadRadio" data-toggle="buttons">
               <label class="btn btn-primary radio-button">
                   <input type="radio" name="${Variablename}" value="Yes"></input>
                   Yes
               </label>
               <label class="btn btn-primary radio-button">
                   <input type="radio" name="${Variablename}" value="No"></input>
                   No
               </label>
           </div>
       </div>
   </div>
   <!-- End LogipadRadio -->

Radio group with small radio buttons inline.

..

   Snippet: logipadsmallradio


.. code-block:: xml

   <!-- Start LogipadSmallRadio -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <br></br>
           <div class="form-check form-check-inline">
               <input class="form-check-input" type="radio" name="${Variablename}" value="${Value1}"></input>
               <label class="form-check-label">
                   <i class="cr-icon glyphicon"></i>
                   ${Value1}
               </label>
           </div>

           <div class="form-check form-check-inline">
               <input class="form-check-input" type="radio" name="${Variablename}" value="${Value2}"></input>
               <label class="form-check-label">
                   <i class="cr-icon glyphicon"></i>
                   ${Value2}
               </label>
           </div>

           <div class="form-check form-check-inline">
               <input class="form-check-input" type="radio" name="${Variablename}" value="${Value3}"></input>
               <label class="form-check-label">
                   <i class="cr-icon glyphicon"></i>
                   ${Value3}
               </label>
           </div>
       </div>
   </div>
   <!-- End LogipadSmallRadio -->

Checkboxes
----------

Checkbox with a label (\ **Value**\ ) on the right side.

..

   Snippet: logipadcheckbox1


.. code-block:: xml

   <!-- Start Logipadcheckbox1 -->
   <div class="col-sm-${width}">
       <div class="form-check">
           <input class="form-check-input" type="checkbox" name="${Variablename}" value="${Value}"></input>
           <label class="form-check-label">
               <i class="cr-icon glyphicon"></i>
               ${Value}
           </label>
       </div>
   </div>
   <!-- End Logipadcheckbox1 -->

Checkbox to open an edit field for not listed opions with the text **Other** on the right side.

..

   Snippet: logipadcheckbox1other


.. code-block:: xml

   <!-- Start Logipadcheckbox1other -->
   <div class="other-col col-sm-${width}">
       <div class="form-check">
           <input class="form-check-input toggleOther" type="checkbox" name="chk${Variablename}"></input>
           <label class="form-check-label">
               <i class="cr-icon glyphicon"></i>
               Other
           </label>
       </div>
       <p></p>
       <div class="collapse" style="padding-left: 20px">
           <input type="text" class="form-control" name="${Variablename}"></input>
           <p></p>
       </div>
   </div>
   <!-- End Logipadcheckbox1other -->

Checkbox with a label (\ **Value**\ ) on the left side.

..

   Snippet: logipadcheckbox2


.. code-block:: xml

   <!-- Start Logipadcheckbox2 -->
   <div class="col-sm-${width}">
       <div class="row">
           <div class="col-sm-10">
               <label class="form-check-label">
                   <i class="cr-icon glyphicon"></i>
                   ${Value}
               </label>
           </div>
           <div class="col-sm-2">
               <div class="form-check">
                   <input class="form-check-input" type="checkbox" name="${Variablename}" value="${Value}"></input>
               </div>
           </div>
       </div>
   </div>
   <!-- End Logipadcheckbox2 -->

Checkbox to open an edit field for not listed opions with the text **Other** on the left side.

..

   Snippet: logipadcheckbox2other


.. code-block:: xml

   <!-- Start Logipadcheckbox2other -->
   <div class="other-col col-sm-${width}">
       <div class="row">
           <div class="col-sm-10">
               <label class="form-check-label">
                   <i class="cr-icon glyphicon"></i>
                   Other
               </label>
               <div class="collapse" style="padding-right: 20px">
                   <p></p>
                   <input type="text" class="form-control" name="${Variablename}"></input>
                   <p></p>
               </div>
           </div>
           <div class="col-sm-2">
               <div class="form-check">
                   <input class="form-check-input toggleOther" type="checkbox" name="chk${Variablename}"></input>
               </div>
           </div>
       </div>
   </div>
   <!-- End Logipadcheckbox2other -->

Datepicker
----------

Date picker with label and data field.
The date needs to have a value because the attribute required is set.

..

   Snippet: logipaddatepicker


.. code-block:: xml

   <!-- Start LogipadDatepicker -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="date" class="form-control form_date" name="${Variablename}" required="required"></input>
       </div>
   </div>
   <!-- End LogipadDatepicker -->

Timepicker
----------

Timepicker with label and data field.
The time needs to have a value because the attribute required is set.

..

   Snippet: logipadtimepicker


.. code-block:: xml

   <!-- Start LogipadTimepicker -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="time" class="form-control form_time" name="${Variablename}" required="required"></input>
       </div>
   </div>
   <!-- End LogipadTimepicker -->

DateTimepicker
--------------

DateTimepicker with label and data field.
The date and time needs to have a value because the attribute required is set.

..

   Snippet: logipaddatetimepicker


.. code-block:: xml

   <!-- Start LogipadDateTimepicker -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="datetime-local" class="form-control form_datetime" name="${Variablename}" required="required"></input>
       </div>
   </div>
   <!-- End LogipadDateTimepicker -->

Periodpicker
------------

Periodpicker with label and data field.
The period needs to have a value because the attribute required is set.

..

   Snippet: logipadperiodpicker


.. code-block:: xml

   <!-- Start LogipadPeriodpicker -->
   <div class="col-sm-${width}">
       <div class="form-group">
           <label class="control-label">
               <i class="glyphicon"></i>
               ${Labeltext}
           </label>
           <input type="cdate" class="form-control form_time2" name="${Variablename}" required="required"></input>
       </div>
   </div>
   <!-- End LogipadPeriodpicker -->

Textarea
--------

Input area with with a given number of rows and field name 'Suggestions' in template.xml.
The field will automatically grow if more rows are entered.

..

   Snippet: logipadtextarea


.. code-block:: xml

   <!-- Start LogipadTextArea -->
   <div class="row">
       <div class="col-sm-12">
           <div class="form-group">
               <label class="control-label">
                   ${Labeltext}
               </label>
               <textarea type="text" name="${Variablename}" class="form-control" rows="${Rows}" cols="90" onkeyup="AutoGrowTextArea(this);"></textarea>
           </div>
       </div>
   </div>
   <!-- End LogipadTextArea -->

Attach picture with scaling
---------------------------

Attach picture function with scaling and preview.
The Select field needs to have the **name**.
The button needs to have the **name** '{picture-name}-button'.
The label for the filename needs to have the **name** '{picture-name}-filename'.
The preview needs to have the **name** '{picture-name}'.

..

   Snippet: logipadpicture


.. code-block:: xml

   <!-- Start LogipadPicture -->
   <div class="col-sm-row">
       <div class="col-sm-5">
           <label class="control-label d-print-none">
               <i class="glyphicon"></i>
               ATTACHMENTS
           </label>
           <select class="lp-selectpicker form-control d-print-none selected" name="${SelectName}" onChange="setCompression(this);">
               <option value="20" selected="selected">small size</option>
               <option value="40">medium size</option>
               <option value="60">large size</option>
               <option value="80">original size</option>
               <option value="100">original quality</option>
           </select>
       </div>
   </div>
   <div class="col-sm-row">
       <div class="col-sm-5">
           <div class="card" style="width: 100%">
               <div class="embed-responsive embed-responsive-16by9">
                   <img class="upload-image-preview" src="" name="${Variablename}"></img>
               </div>
           </div>
       </div>
   </div>
   <div class="col-sm-row d-print-none">
       <div class="col-sm-5">
           <label class="control-label">
               <i class="glyphicon"></i>
               File Selection
           </label>
           <div class="input-group">
               <span class="input-group-btn">
                   <button name="${Variablename}-button" type="button" class="lp-file-browse btn btn-warning form-control">
                       <span class="glyphicon glyphicon-file"></span>
                   </button>
               </span>
               <input type="file" class="form-control lp-image lp-filename" name="${Variablename}" style="display:none;"></input>
               <input type="text" disabled="Disabled" name="${Variablename}-filename" placeholder="File not selected" class="form-control"></input>
           </div>
       </div>
   </div>
   <!-- End LogipadPicture -->

Navigation Tabs
---------------

Tab-menu with two tabs default. Any number of tabs can be added.
The navigation-tabs needs to have a tab-name.

..

   Snippet: logipadnavtab


.. code-block:: xml

   <!-- Start LogipadNavTabs -->
   <ul class="nav nav-tabs">
       <li class="nav-item">
           <a class="nav-link active">${Tabname1}</a>
       </li>
       <li class="nav-item">
           <a class="nav-link">${Tabname2}</a>
       </li>
   </ul>
   <div class="tab-content">
       <div name="${Variablename1}" class="tab-pane fade show active">
           Place Content for tab ${Variablename1} here
       </div>
       <div name="${Variablename2}" class="tab-pane fade">
           Place Content for tab ${Variablename2} here
       </div>
   </div>
   <!-- End LogipadNavTabs -->

Tab-menu with one tab which can be extended dynamically by a number (\ **Max**\ ) of tabs. 
**Variablename** specifies the name of the content in the tabs (possibly in plural), **Variablename1** specifies the name of the individual tab.

..

   Snippet: logipadnavtabaddedtabs


.. code-block:: xml

   <!-- Start LogipadAdddedNavTabs -->
   <ul class="nav nav-tabs" role="tablist">
       <li class="nav-item">
           <a class="nav-link active" role="tab">${Tabname}</a>
       </li>
       <li class="nav-item">
           <a class="nav-link link-add-section">+ Add</a>
       </li>
       <li class="nav-item">
           <a class="nav-link link-delete-section">- Delete</a>
       </li>
   </ul>
   <div class="tab-content dynamic-tab" name=\"${Variablename}\" max="${Max}">
       <div class="tab-pane fade show active" name="${Variablename1}" role="tabpanel">
       </div>
   </div>
   <!-- End LogipadAdddedNavTabs -->

Table
-----

Table with a header and one content row. Any number of table-rows can be added.
If the table should have no border remove class **table-bordered**.
To align the label of single column to the left remove the style of the **th**\ -Tag.

..

   Snippet: logipadtable


.. code-block:: xml

   <!-- Start LogipadTable -->
   <div class="col-sm-12" style="height: 20px;"></div>
   <div class="col-sm-12">
       <table class="table table-bordered">
           <thead>
               <tr>
                   <th style="text-align: center;">${Labeltext1}</th>
                   <th style="text-align: center;">${Labeltext2}</th>
                   <th style="text-align: center;">${Labeltext3}</th>
               </tr>
           </thead>
           <tbody>
               <tr>
                   <td>${Content1}</td>
                   <td>${Content2}</td>
                   <td>${Content3}</td>
               </tr>
           </tbody>
       </table>
   </div>
   <!-- Spacing of 20px to next control -->
   <div class="col-xs-12" style="height: 20px;"></div>
   <!-- End LogipadTable -->

Table with buttons to add and delete rows
-----------------------------------------

Table with a header and a defined number (\ **addedRows**\ ) of content rows.
A define number of table-rows can be add and delete (\ **maxRow**\ ) by using the buttons.
**VariablenameTable** specifies the name of the content in the table (possibly in plural), **Variablename** specifies the name of the individual table row.

..

   Snippet: logipadtableaddedrows


.. code-block:: xml

   <!-- Start LogipadTableAddedRows -->
   <div class="col-sm-12">
       <table class="table" name="${VariablenameTable}" maxRow="${MaxRows}" addedRows="${AddedRows}">
           <thead>
               <th>
                   <i class="glyphicon"></i> ${Labeltext1}
               </th>
               <th>
                   <i class="glyphicon"></i> ${Labeltext2}
               </th>
               <th>
                   <i class="glyphicon"></i> ${Labeltext3}
               </th>
           </thead>
           <tbody>
               <tr name="${Variablename}">
                   <td>
                       ${Content1}
                   </td>
                   <td>
                       ${Content2}
                   </td>
                   <td>
                       ${Content3}
                   </td>
               </tr>
           </tbody>
       </table>
       <button type="button" class="btn btn-light btn-sm lp-add-table-row">
           <span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Add Row
       </button>
       <button type="button" class="btn btn-light btn-sm lp-del-table-row">
           <span class="glyphicon glyphicon-minus" aria-hidden="true"></span> Del Row
       </button>
       <p></p>
   </div>
   <!-- End LogipadTableAddedRows -->

Definitions for xsl.json
------------------------

Please copy the following code to the xsl user snippets to enable th snippeds inside the editor to enable it.

..

   To access the file please use the following menu steps inside Microsoft Visual Studio Code
   File -> Preferences -> User Snippets
   Here select XSL as language and paste the content into the file.
   If you are using a MAC the import menu is located under
   Code -> Preferences -> User Snippets


.. code-block:: json

   {
       "LogipadHeader": {
           "prefix": "logipadheader",
           "body": [
               "<!-- START OF HEADER-->",
               "<p></p>",
               "<div class=\"row\">",
               "    <div class=\"col-sm-9\">",
               "        <label class=\"control-label Title\">",
               "            ${FormName}",
               "        </label>",
               "    </div>",
               "    <div class=\"col-sm-3\">",
               "        <div class=\"row\">",
               "            <div class=\"col-sm-12\" align=\"right\">",
               "                <img src=\"./images/logipad_aero.png\" width=\"200px\"></img>",
               "            </div>",
               "        </div>",
               "        <div class=\"row\">",
               "            <div class=\"col-sm-12\" align=\"right\">",
               "                eForm Version 1.2",
               "            </div>",
               "        </div>",
               "    </div>",
               "</div>",
               "<p></p>",
               "<!-- END OF HEADER-->"
           ],
           "description": "Insert a form header section"
       },
       "LogipadSection": {
           "prefix": "logipadsection",
           "body": [
               "<!-- START Section ${Sectionname} -->",
               "<div class=\"row\">",
               "    <div class=\"col-sm-12\">",
               "        <div class=\"SectionHeader SectionTitle\">",
               "            ${Sectionname}",
               "        </div>",
               "        <p></p>",
               "    </div>",
               "</div>",
               "${Content}",
               "<!-- END Section ${Sectionname} -->"
           ],
           "description": "Insert a section header."
       },
       "LogipadInput": {
           "prefix": "logipadinput",
           "body": [
               "<!-- Start LogipadInput -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"text\" class=\"form-control\" name=\"${Variablename}\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadInput -->"
           ],
           "description": "Insert a input field"
       },
       "LogipadInputRequired": {
           "prefix": "logipadinputrequired",
           "body": [
               "<!-- Start LogipadInputRequired -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"text\" class=\"form-control\" name=\"${Variablename}\" required=\"required\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadInputRequired -->"
           ],
           "description": "Insert a required input field"
       },
       "LogipadInput3LC": {
           "prefix": "logipadinput3lc",
           "body": [
               "<!-- Start LogipadInput3LC -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"three-lc\" class=\"form-control\" name=\"${Variablename}\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadInput3LC -->"
           ],
           "description": "Insert a input field for 3lc"
       },
       "LogipadInputNumber": {
           "prefix": "logipadinputnumber",
           "body": [
               "<!-- Start LogipadInputNumber -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"number\" class=\"form-control\" name=\"${Variablename}\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadInputNumber -->"
           ],
           "description": "Insert a input field for numbers"
       },
       "LogipadSelect1": {
           "prefix": "logipadselect1",
           "body": [
               "<!-- Start LogipadSelect1 -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <select class=\"selectpicker form-control\" name=\"${Variablename}\" required=\"required\" data-live-search=\"true\" title=\"Select...\"></select>",
               "    </div>",
               "</div>",
               "<!-- End LogipadSelect1 -->"
           ],
           "description": "Insert a select. Prefilled form backend"
       },
       "LogipadSelect2": {
           "prefix": "logipadselect2",
           "body": [
               "<!-- Start LogipadSelect2 -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <select class=\"selectpicker form-control\" name=\"${Variablename}\" title=\"Select ...\">",
               "            <option value=\"${Option1}\">${Option1}</option>",
               "            <option value=\"${Option2}\">${Option2}</option>",
               "            <option value=\"Other\">Other ...</option>",
               "        </select>",
               "    </div>",
               "</div>",
               "<!-- End LogipadSelect2 -->"
           ],
           "description": "Insert a select."
       },
       "LogipadRadio": {
           "prefix": "logipadradio",
           "body": [
               "<!-- Start LogipadRadio -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <br></br>",
               "        <div class=\"btn-group btn-group-toggle LogipadRadio\" data-toggle=\"buttons\">",
               "            <label class=\"btn btn-primary radio-button\">",
               "                <input type=\"radio\" name=\"${Variablename}\" value=\"Yes\"></input>",
               "                Yes",
               "            </label>",
               "            <label class=\"btn btn-primary radio-button\">",
               "                <input type=\"radio\" name=\"${Variablename}\" value=\"No\"></input>",
               "                No",
               "            </label>",
               "        </div>",
               "    </div>",
               "</div>",
               "<!-- End LogipadRadio -->"
           ],
           "description": "Insert a radio group."
       },
       "LogipadSmallRadio": {
           "prefix": "logipadsmallradio",
           "body": [
               "<!-- Start LogipadSmallRadio -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <br></br>",
               "        <div class=\"form-check form-check-inline\">",
               "            <input class=\"form-check-input\" type=\"radio\" name=\"${Variablename}\" value=\"${Value1}\"></input>",
               "            <label class=\"form-check-label\">",
               "                <i class=\"cr-icon glyphicon\"></i>",
               "                ${Value1}",
               "            </label>",
               "        </div>",
               "        ",
               "        <div class=\"form-check form-check-inline\">",
               "            <input class=\"form-check-input\" type=\"radio\" name=\"${Variablename}\" value=\"${Value2}\"></input>",
               "            <label class=\"form-check-label\">",
               "                <i class=\"cr-icon glyphicon\"></i>",
               "                ${Value2}",
               "            </label>",
               "        </div>",
               "        ",
               "        <div class=\"form-check form-check-inline\">",
               "            <input class=\"form-check-input\" type=\"radio\" name=\"${Variablename}\" value=\"${Value3}\"></input>",
               "            <label class=\"form-check-label\">",
               "                <i class=\"cr-icon glyphicon\"></i>",
               "                ${Value3}",
               "            </label>",
               "        </div>",
               "    </div>",
               "</div>",
               "<!-- End LogipadSmallRadio -->"
           ],
           "description": "Insert a radio group with three small buttons."
       },
       "LogipadCheckbox1": {
           "prefix": "logipadcheckbox1",
           "body": [
               "<!-- Start Logipadcheckbox1 -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-check\">",
               "        <input class=\"form-check-input\" type=\"checkbox\" name=\"${Variablename}\" value=\"${Value}\"></input>",
               "        <label class=\"form-check-label\">",
               "            <i class=\"cr-icon glyphicon\"></i>",
               "            ${Value}",
               "        </label>",
               "    </div>",
               "</div>",
               "<!-- End Logipadcheckbox1 -->"
           ],
           "description": "Insert a checkbox with a label. checbox on the left side of the text."
       },
       "LogipadCheckbox1other": {
           "prefix": "logipadcheckbox1other",
           "body": [
               "<!-- Start Logipadcheckbox1other -->",
               "<div class=\"other-col col-sm-${width}\">",
               "    <div class=\"form-check\">",
               "        <input class=\"form-check-input toggleOther\" type=\"checkbox\" name=\"chk${Variablename}\"></input>",
               "        <label class=\"form-check-label\">",
               "            <i class=\"cr-icon glyphicon\"></i>",
               "            Other",
               "        </label>",
               "    </div>",
               "    <p></p>",
               "    <div class=\"collapse\" style=\"padding-left: 20px\">",
               "        <input type=\"text\" class=\"form-control\" name=\"${Variablename}\"></input>",
               "        <p></p>",
               "    </div>",
               "</div>",
               "<!-- End Logipadcheckbox1other -->"
           ],
           "description": "Insert a checkbox with a label and edit box. checbox on the left side of the text."
       },
       "LogipadCheckbox2": {
           "prefix": "logipadcheckbox2",
           "body": [
               "<!-- Start Logipadcheckbox2 -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"row\">",
               "        <div class=\"col-sm-10\">",
               "            <label class=\"form-check-label\">",
               "                <i class=\"cr-icon glyphicon\"></i>",
               "                ${Value}",
               "            </label>",
               "        </div>",
               "        <div class=\"col-sm-2\">",
               "            <div class=\"form-check\">",
               "                <input class=\"form-check-input\" type=\"checkbox\" name=\"${Variablename}\" value=\"${Value}\"></input>",
               "            </div>",
               "        </div>",
               "    </div>",
               "</div>",
               "<!-- End Logipadcheckbox2 -->"
           ],
           "description": "Insert a checkbox with a label. checbox on the right side of the text."
       },
       "LogipadCheckbox2other": {
           "prefix": "logipadcheckbox2other",
           "body": [
               "<!-- Start Logipadcheckbox2other -->",
               "<div class=\"other-col col-sm-${width}\">",
               "    <div class=\"row\">",
               "        <div class=\"col-sm-10\">",
               "            <label class=\"form-check-label\">",
               "                <i class=\"cr-icon glyphicon\"></i>",
               "                Other",
               "            </label>",
               "            <div class=\"collapse\" style=\"padding-right: 20px\">",
               "                <p></p>",
               "                <input type=\"text\" class=\"form-control\" name=\"${Variablename}\"></input>",
               "                <p></p>",
               "            </div>",
               "        </div>",
               "        <div class=\"col-sm-2\">",
               "            <div class=\"form-check\">",
               "                <input class=\"form-check-input toggleOther\" type=\"checkbox\" name=\"chk${Variablename}\"></input>",
               "            </div>",
               "        </div>",
               "    </div>",
               "</div>",
               "<!-- End Logipadcheckbox2other -->"
           ],
           "description": "Insert a checkbox with a label and edit box. checbox on the right side of the text."
       },
       "LogipadDatepicker": {
           "prefix": "logipaddatepicker",
           "body": [
               "<!-- Start LogipadDatepicker -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"date\" class=\"form-control form_date\" name=\"${Variablename}\" required=\"required\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadDatepicker -->"
           ],
           "description": "Insert a date picker."
       },
       "LogipadTimepicker": {
           "prefix": "logipadtimepicker",
           "body": [
               "<!-- Start LogipadTimepicker -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"time\" class=\"form-control form_time\" name=\"${Variablename}\" required=\"required\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadTimepicker -->"
           ],
           "description": "Insert a time picker."
       },
       "LogipadDateTimepicker": {
           "prefix": "logipaddatetimepicker",
           "body": [
               "<!-- Start LogipadDateTimepicker -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"datetime-local\" class=\"form-control form_datetime\" name=\"${Variablename}\" required=\"required\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadDateTimepicker -->"
           ],
           "description": "Insert a datetime picker."
       },
       "LogipadPeriodpicker": {
           "prefix": "logipadperiodpicker",
           "body": [
               "<!-- Start LogipadPeriodpicker -->",
               "<div class=\"col-sm-${width}\">",
               "    <div class=\"form-group\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            ${Labeltext}",
               "        </label>",
               "        <input type=\"cdate\" class=\"form-control form_time2\" name=\"${Variablename}\" required=\"required\"></input>",
               "    </div>",
               "</div>",
               "<!-- End LogipadPeriodpicker -->"
           ],
           "description": "Insert a period picker."
       },
       "LogipadTextArea": {
           "prefix": "logipadtextarea",
           "body": [
               "<!-- Start LogipadTextArea -->",
               "<div class=\"row\">",
               "    <div class=\"col-sm-12\">",
               "        <div class=\"form-group\">",
               "            <label class=\"control-label\">",
               "                ${Labeltext}",
               "            </label>",
               "            <textarea type=\"text\" name=\"${Variablename}\" class=\"form-control\" rows=\"${Rows}\" cols=\"90\" onkeyup=\"AutoGrowTextArea(this);\"></textarea>",
               "        </div>",
               "    </div>",
               "</div>",
               "<!-- End LogipadTextArea -->"
           ],
           "description": "Insert a date picker."
       },
       "LogipadPicture": {
           "prefix": "logipadpicture",
           "body": [
               "<!-- Start LogipadPicture -->",
               "<div class=\"col-sm-row\">",
               "    <div class=\"col-sm-5\">",
               "        <label class=\"control-label d-print-none\">",
               "            <i class=\"glyphicon\"></i>",
               "            ATTACHMENTS",
               "        </label>",
               "        <select class=\"lp-selectpicker form-control d-print-none selected\" name=\"${SelectName}\" onChange=\"setCompression(this);\">",
               "            <option value=\"20\" selected=\"selected\">small size</option>",
               "            <option value=\"40\">medium size</option>",
               "            <option value=\"60\">large size</option>",
               "            <option value=\"80\">original size</option>",
               "            <option value=\"100\">original quality</option>",
               "        </select>",
               "    </div>",
               "</div>",
               "<div class=\"col-sm-row\">",
               "    <div class=\"col-sm-5\">",
               "        <div class=\"card\" style=\"width: 100%\">",
               "            <div class=\"embed-responsive embed-responsive-16by9\">",
               "                <img class=\"upload-image-preview\" src=\"\" name=\"${Variablename}\"></img>",
               "            </div>",
               "        </div>",
               "    </div>",
               "</div>",
               "<div class=\"col-sm-row d-print-none\">",
               "    <div class=\"col-sm-5\">",
               "        <label class=\"control-label\">",
               "            <i class=\"glyphicon\"></i>",
               "            File Selection",
               "        </label>",
               "        <div class=\"input-group\">",
               "            <span class=\"input-group-btn\">",
               "                <button name=\"${Variablename}-button\" type=\"button\" class=\"lp-file-browse btn btn-warning form-control\">",
               "                    <span class=\"glyphicon glyphicon-file\"></span>",
               "                </button>",
               "            </span>",
               "            <input type=\"file\" class=\"form-control lp-image lp-filename\" name=\"${Variablename}\" style=\"display:none;\"></input>",
               "            <input type=\"text\" disabled=\"Disabled\" name=\"${Variablename}-filename\" placeholder=\"File not selected\" class=\"form-control\"></input>",
               "        </div>",
               "    </div>",
               "</div>",
               "<!-- End LogipadPicture -->"
           ],
           "description": "Attach a picture."
       },
       "LogipadNavTab": {
           "prefix": "logipadnavtab",
           "body": [
               "<!-- Start LogipadNavTabs -->",
               "<ul class=\"nav nav-tabs\">",
               "    <li class=\"nav-item\">",
               "        <a class=\"nav-link active\">${Tabname1}</a>",
               "    </li>",
               "    <li class=\"nav-item\">",
               "        <a class=\"nav-link\">${Tabname2}</a>",
               "    </li>",
               "</ul>",
               "<div class=\"tab-content\">",
               "    <div name=\"${Variablename1}\" class=\"tab-pane fade show active\">",
               "        Place Content for tab ${Variablename1} here",
               "    </div>",
               "    <div name=\"${Variablename2}\" class=\"tab-pane fade\">",
               "        Place Content for tab ${Variablename2} here",
               "    </div>",
               "</div>",
               "<!-- End LogipadNavTabs -->"
           ],
           "description": "Insert a navigation tab."
       },
       "LogipadNavTabAddedTabs": {
           "prefix": "logipadnavtabaddedtabs",
           "body": [
               "<!-- Start LogipadAdddedNavTabs -->",
               "<ul class=\"nav nav-tabs\" role=\"tablist\">",
               "    <li class=\"nav-item\">",
               "        <a class=\"nav-link active\" role=\"tab\">${Tabname}</a>",
               "    </li>",
               "    <li class=\"nav-item\">",
               "        <a class=\"nav-link link-add-section\">+ Add</a>",
               "    </li>",
               "    <li class=\"nav-item\">",
               "        <a class=\"nav-link link-delete-section\">- Delete</a>",
               "    </li>",
               "</ul>",
               "<div class=\"tab-content dynamic-tab\" name=\"${Variablename}\" max=\"${Max}\">",
               "    <div class=\"tab-pane fade show active\" name=\"${Variablename1}\" role=\"tabpanel\">",
               "    </div>",
               "</div>",
               "<!-- End LogipadAdddedNavTabs -->"
           ],
           "description": "Insert a navigation tab  with buttons to add a new tab."
       },
       "LogipadTable": {
           "prefix": "logipadtable",
           "body": [
               "<!-- Start LogipadTable -->",
               "<div class=\"col-sm-12\" style=\"height: 20px;\"></div>",
               "<div class=\"col-sm-12\">",
               "    <table class=\"table table-bordered\">",
               "        <thead>",
               "            <tr>",
               "                <th style=\"text-align: center;\">${Labeltext1}</th>",
               "                <th style=\"text-align: center;\">${Labeltext2}</th>",
               "                <th style=\"text-align: center;\">${Labeltext3}</th>",
               "            </tr>",
               "        </thead>",
               "        <tbody>",
               "            <tr>",
               "                <td>${Content1}</td>",
               "                <td>${Content2}</td>",
               "                <td>${Content3}</td>",
               "            </tr>",
               "        </tbody>",
               "    </table>",
               "</div>",
               "<!-- Spacing of 20px to next control -->",
               "<div class=\"col-xs-12\" style=\"height: 20px;\"></div>",
               "<!-- End LogipadTable -->"
           ],
           "description": "Insert a bordered table."
       },
       "LogipadTableAddedRows": {
           "prefix": "logipadtableaddedrows",
           "body": [
               "<!-- Start LogipadTableAddedRows -->",
               "<div class=\"col-sm-12\">",
               "    <table class=\"table\" name=\"${VariablenameTable}\" maxRow=\"${MaxRows}\" StartValue=\"${StartValue}\" addedRows=\"${AddedRows}\">",
               "        <thead>",
               "            <th>",
               "                <i class=\"glyphicon\"></i> ${Labeltext1}",
               "            </th>",
               "            <th>",
               "                <i class=\"glyphicon\"></i> ${Labeltext2}",
               "            </th>",
               "            <th>",
               "                <i class=\"glyphicon\"></i> ${Labeltext3}",
               "            </th>",
               "        </thead>",
               "        <tbody>",
               "            <tr name=\"${Variablename}\">",
               "                <td>",
               "                    ${Content1}",
               "                </td>",
               "                <td>",
               "                    ${Content2}",
               "                </td>",
               "                <td>",
               "                    ${Content3}",
               "                </td>",
               "            </tr>",
               "        </tbody>",
               "    </table>",
               "    <button type=\"button\" class=\"btn btn-light btn-sm lp-add-table-row\">",
               "        <span class=\"glyphicon glyphicon-plus\" aria-hidden=\"true\"></span> Add Row",
               "    </button>",
               "    <button type=\"button\" class=\"btn btn-light btn-sm lp-del-table-row\">",
               "        <span class=\"glyphicon glyphicon-minus\" aria-hidden=\"true\"></span> Del Row",
               "    </button>",
               "    <p></p>",
               "</div>",
               "<!-- End LogipadTableAddedRows -->"
           ],
           "description": "Insert a table with buttons to add and delete rows."
       },
       "LogipadDraw": {
           "prefix": "logipaddraw",
           "body": [
               "<!-- Start LogipadDraw -->",
               "<div class=\"col-sm-12\">",
               "    <div class=\"signature-pad center-block\">",
               "        <div class=\"signature-pad--body\" width=\"${ImageWidth}\" height=\"${ImageHeight}\">",
               "            <img src=\"images/${Imagename}\" width=\"${ImageWidth}\" height=\"${ImageHeight}\" alt=\"\"></img>",
               "            <canvas name=\"${Variablename}\" class=\"sp-canvas\"></canvas>",
               "        </div>",
               "        <div class=\"signature-pad--footer btn-toolbar\" role=\"toolbar\">",
               "            <button type=\"button\" class=\"btn btn-secondary\" data-action=\"clear\">Clear</button>",
               "            <button type=\"button\" class=\"btn btn-primary\" data-action=\"save\">Save changes</button>",
               "        </div>",
               "    </div>",
               "    <p></p>",
               "</div>",
               "<!-- End LogipadDraw -->"
           ],
           "description": "Insert an area with an image that can be painted on."
       },
       "LogipadSignature": {
           "prefix": "logipadsignature",
           "body": [
               "<!-- Start LogipadSignature -->",
               "<div class=\"col-sm-12\">",
               "    <div class=\"signature-pad\">",
               "        <div class=\"signature-pad--body\">",
               "            <canvas name=\"${Variablename}\" class=\"sp-canvas\"></canvas>",
               "        </div>",
               "        <div class=\"signature-pad--footer btn-toolbar\" role=\"toolbar\">",
               "            <button type=\"button\" class=\"btn btn-secondary\" data-action=\"clear\">Clear</button>",
               "            <button type=\"button\" class=\"btn btn-primary\" data-action=\"save\">Save changes</button>",
               "        </div>",
               "    </div>",
               "</div>",
               "<!-- End LogipadSignature -->"
           ],
           "description": "Insert an area where a signature can be placed."
       }
   }
