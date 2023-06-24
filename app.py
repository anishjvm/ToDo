from flask import Flask, g, escape, session, redirect, render_template, request, jsonify, Response

app = Flask(__name__)

app.secret_key='Anish'


