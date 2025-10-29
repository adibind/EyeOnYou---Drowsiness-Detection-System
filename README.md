<h1><b>EyeOnYou - Drowsiness Detection System</b></h1>

<h2><b>Overview</b></h2>
<p><b>EyeOnYou</b> is a real-time drowsiness detection system that monitors driver alertness by analyzing <b>Eye Aspect Ratio (EAR)</b> through webcam input. If drowsiness is detected, an alarm is triggered to alert the driver.</p>

<h2><b>Features</b></h2>
<ul>
  <li>Real-time face and eye detection using <b>dlib</b> and <b>OpenCV</b>.</li>
  <li><b>Eye Aspect Ratio (EAR)</b> calculation to detect drowsiness.</li>
  <li>Audio alert triggered when the user shows signs of drowsiness.</li>
  <li>Adjustable detection threshold and frame count for custom sensitivity.</li>
</ul>

<h2><b>Requirements</b></h2>
<ul>
  <li><b>Python 3.x</b></li>
  <li><b>OpenCV</b></li>
  <li><b>Dlib</b></li>
  <li><b>Scipy</b></li>
  <li><b>Imutils</b></li>
  <li><b>Pygame</b></li>
</ul>

<h2><b>How to Run</b></h2>
<ol>
  <li>Clone this repository:</li>
  <pre><code>git clone https://github.com/your-username/your-repo-name.git</code></pre>

  <li>Install the required packages:</li>
  <pre><code>pip install -r requirements.txt</code></pre>

  <li>Download the <code>shape_predictor_68_face_landmarks.dat</code> model from <a href="http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2">here</a>, extract it, and place it in the <b>models</b> directory.</li>

  <li>Run the script:</li>
  <pre><code>python Drowsiness_Detection.py --show_video</code></pre>

  <li>Press <code>q</code> to stop the detection.</li>
</ol>

<h2><b>Customization</b></h2>
<p>You can adjust the sensitivity of the detection by modifying the following parameters:</p>
<ul>
  <li><b>Threshold</b>: Adjust the EAR threshold for drowsiness detection using the <code>--threshold</code> argument.</li>
  <li><b>Frames</b>: Set the number of consecutive frames for detection using the <code>--frames</code> argument.</li>
</ul>

<h2><b>Example</b></h2>
<pre><code>python Drowsiness_Detection.py --threshold 0.25 --frames 20 --show_video</code></pre>

<h2><b>License</b></h2>
<p>This project is licensed under the <b>MIT License</b>.</p>
