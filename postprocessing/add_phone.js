/**
 * This module loads the resume.json from the repo root dir and adds my phone number pulled from .env PHONE_NUMBER
 * to the contact section. It then saves the file as resume_phone.json in the root dir
 */

const fs = require('fs');
const path = require('path');
const dotenv = require('dotenv');
const { promisify } = require('util');
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

const envPath = path.join(__dirname, '../.env');
dotenv.config({ path: envPath });

const resumePath = path.join(__dirname, '../resume.json');
const resumePhonePath = path.join(__dirname, '../resume_phone.json');

const addPhone = async () => {
    try {
        const resume = await readFile(resumePath);
        const resumeObj = JSON.parse(resume);
        const phone = process.env.PHONE_NUMBER;
        resumeObj.basics.phone = phone;
        await writeFile(resumePhonePath, JSON.stringify(resumeObj, null, 2));
        console.log('Phone number added to resume_phone.json');
    } catch (err) {
        console.log(err);
    }
};

addPhone();