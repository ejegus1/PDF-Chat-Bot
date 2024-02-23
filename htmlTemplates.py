css = '''
<style>
    .chat-message {
        padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
    }
    .chat-message.user {
        font: 18px "Poppins", sans-serif;
        background-color: #0D4599;
    }
    .chat-message.bot {
        font: 18px "Poppins", sans-serif;
        background-color: #006AFF;
    }
    .chat-message .avatar {
        width: 20%;
    }
    .chat-message .avatar img {
        max-width: 78px;
        max-height: 78px;
        border-radius: 50%;
        object-fit: cover;
    }
    .chat-message .message {
        width: 80%;
        padding: 0 1.5rem;
        color: #FFFFFF;
    }
    .stTextInput {
        position: fixed;
        bottom: 30px;
        z-index: 1;
        background-color: #F2A619;
        padding: 10px;
    }
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/f6/Lol_question_mark.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
