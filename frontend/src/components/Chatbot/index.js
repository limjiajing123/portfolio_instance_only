import React, { useState, useRef, useEffect, useCallback } from 'react';
import styled from 'styled-components';
import { FaRobot, FaArrowsAlt, FaTrash } from 'react-icons/fa';
import axios from 'axios';

// Styled components
const ChatbotButton = styled.button`
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 2000;
  background-color: rgb(111, 0, 255);
  color: white;
  border: none;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s;

  &:hover {
    background-color: #0056b3;
  }

  &:focus {
    outline: none;
  }
`;

const ChatbotWindow = styled.div`
  position: fixed;
  bottom: 30px;
  right: 100px;
  width: 450px;
  height: 600px;
  background-color: #fff;
  border: 2px solid rgb(132, 0, 255);
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  z-index: 1000;
  resize: both;

  @media (max-width: 600px) {
    width: 90%;
    height: 70%;
    right: 30px;
    bottom: calc(30px + 60px);
  }

  .resize-handle {
    position: absolute;
    top: 0;
    left: 0;
    width: 50px;
    height: 44px;
    cursor: nwse-resize;
    background: rgba(34, 7, 235, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    border-top-left-radius: 15px;
  }

  .chat-header {
    position: relative;
    background-color: rgb(115, 17, 160);
    color: #fff;
    padding: 10px;
    font-weight: bold;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .chat-header button {
    position: absolute;
    right: 10px;
    background: transparent;
    border: none;
    cursor: pointer;
    color: white;
  }

  .chat-body {
    flex: 1;
    padding: 10px;
    overflow-y: auto;
    background-color: rgb(166, 121, 192);
    display: flex;
    flex-direction: column;
  }
`;

const ChatInput = styled.form`
  display: flex;
  border-top: 1px solid #ccc;
  padding: 5px;

  input {
    flex: 1;
    padding: 10px;
    border: none;
    outline: none;
    font-size: 1em;
  }

  button {
    padding: 10px;
    border: none;
    background-color: rgb(5, 59, 28);
    color: #fff;
    cursor: pointer;
    border-radius: 8px;

    &:hover {
      background-color: rgb(33, 173, 108);
    }

    &:disabled {
      background-color: grey;
      cursor: not-allowed;
    }
  }
`;

const ChatBubbleUser = styled.div`
  background-color: #d1e7dd;
  color: #0f5132;
  padding: 8px 12px;
  border-radius: 15px;
  max-width: 70%;
  align-self: flex-end;
  margin: 5px 0;
`;

const ChatBubbleBot = styled.div`
  background-color: #f8d7da;
  color: #842029;
  padding: 8px 12px;
  border-radius: 15px;
  max-width: 70%;
  align-self: flex-start;
  margin: 5px 0;
`;

const TypingIndicatorContainer = styled.div`
  display: flex;
  align-items: center;
`;

const Dot = styled.div`
  background-color: #842029;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin: 0 2px;
  animation: blink 1.4s infinite both;

  &:nth-child(2) {
    animation-delay: 0.2s;
  }

  &:nth-child(3) {
    animation-delay: 0.4s;
  }

  @keyframes blink {
    0%, 80%, 100% { opacity: 0; }
    40% { opacity: 1; }
  }
`;

const TypingIndicator = () => (
  <TypingIndicatorContainer>
    <Dot />
    <Dot />
    <Dot />
  </TypingIndicatorContainer>
);

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [userMessage, setUserMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [isBotTyping, setIsBotTyping] = useState(false);
  const windowRef = useRef(null);
  const chatBodyRef = useRef(null);

  const toggleChatbot = () => setIsOpen(!isOpen);

  const handleInputChange = useCallback((e) => {
    setUserMessage(e.target.value);
  }, []);

  const handleClear = useCallback(() => {
    setChatHistory([]);
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (userMessage.trim() === '' || isBotTyping) return;

    const messageToSend = userMessage;
    setUserMessage('');
    setChatHistory((prev) => [...prev, { sender: 'user', message: messageToSend }]);
    setIsBotTyping(true);

    try {
      const response = await axios.post('https://limjiajing.com/api/chat', { message: messageToSend });
      setChatHistory((prev) => [
        ...prev,
        { sender: 'bot', message: response.data.botResponse }
      ]);
    } catch (error) {
      console.error('Error sending message to backend:', error);
      setChatHistory((prev) => [
        ...prev,
        { sender: 'bot', message: 'I\'m sorry, I am having trouble right now. Please try again later.' }
      ]);
    } finally {
      setIsBotTyping(false);
    }
  };

  useEffect(() => {
    if (chatBodyRef.current) {
      chatBodyRef.current.scrollTop = chatBodyRef.current.scrollHeight;
    }
  }, [chatHistory, isBotTyping]);

  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') setIsOpen(false);
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  useEffect(() => {
    const handleMouseDown = (e) => {
      const startX = e.clientX;
      const startY = e.clientY;
      const startWidth = windowRef.current.offsetWidth;
      const startHeight = windowRef.current.offsetHeight;

      const handleMouseMove = (e) => {
        const newWidth = startWidth - (e.clientX - startX);
        const newHeight = startHeight - (e.clientY - startY);
        windowRef.current.style.width = `${Math.max(200, newWidth)}px`;
        windowRef.current.style.height = `${Math.max(300, newHeight)}px`;
      };

      const handleMouseUp = () => {
        window.removeEventListener('mousemove', handleMouseMove);
        window.removeEventListener('mouseup', handleMouseUp);
      };

      window.addEventListener('mousemove', handleMouseMove);
      window.addEventListener('mouseup', handleMouseUp);
    };

    if (windowRef.current) {
      const resizeHandle = windowRef.current.querySelector('.resize-handle');
      if (resizeHandle) {
        resizeHandle.addEventListener('mousedown', handleMouseDown);
      }
    }
  }, [isOpen]);

  return (
    <>
      <ChatbotButton onClick={toggleChatbot}>
        <FaRobot size={28} />
      </ChatbotButton>

      {isOpen && (
        <ChatbotWindow ref={windowRef}>
          <div className="resize-handle">
            <FaArrowsAlt color="white" size={20} />
          </div>
          <div className="chat-header">
            <span>Chat with Me!</span>
            <button onClick={handleClear}>
              <FaTrash size={20} />
            </button>
          </div>
          <div className="chat-body" ref={chatBodyRef}>
            {chatHistory.map((chat, index) =>
              chat.sender === 'user' ? (
                <ChatBubbleUser key={index}>{chat.message}</ChatBubbleUser>
              ) : (
                <ChatBubbleBot key={index}>{chat.message}</ChatBubbleBot>
              )
            )}
            {isBotTyping && (
              <ChatBubbleBot>
                <TypingIndicator />
              </ChatBubbleBot>
            )}
          </div>
          <ChatInput onSubmit={handleSubmit}>
            <input
              type="text"
              value={userMessage}
              onChange={handleInputChange}
              placeholder="Type a message..."
              disabled={isBotTyping}
            />
            <button type="submit" disabled={isBotTyping}>Send</button>
          </ChatInput>
        </ChatbotWindow>
      )}
    </>
  );
};

export default Chatbot;
