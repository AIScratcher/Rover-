
<div style="visibility=hidden;">
  @author : aiscratch
  @version 0.1.0
</div>
<h1>An Implementation of HTM</h1>
<p>
        The Network of Neurons Model porposed by the
        <a href="https://www.numenta.com">Numenta Inc.</a>
        and there <a href="https://numenta.org">Open Source Community</a>
        I want to refer to them at first because if you want to understand this <br>
        Code you must understand the theory of Hierarchical Temporal Memory.
        Best explanation for easy understanding of how the theory works:<br>
        <a href="https://www.numenta.org/htm-school/">This Video Series</a>
        or for people who like to read:<br>
        <a href="https://www.numenta.com/resources/papers/">Research Papers</a>
</p>

<h2> The Columns / Layer Model </h2>
<p>Think about the Neocortex as a block, consisting of many <br>
   smaller blocks, order in Layers and Columns going through the Layers.<br>
   Then you will have a good idea about how I refer to Layers and Columns in this<br>
   Implementation.The Layer is a group of Neurons that all operate on the same<br>
   input data and pass them through to another Layer for which there output will be<br>
   the input.
</p>
<h2>The single Neuron</h2>
<p>
  A single Neuron receives three inputs that are again two values, so each Neuron<br>
  needs 6 Values to run.
  The Neurons work together with there Layer, to grantee that the Neurons receives
  the right and the whole input.
  The steps are:
  <ol>
  <li>Forward Output calculation</li>
  <li>Context Pooling</li>
  <li>Feedback Pooling</li>
  </ol>
  Every step works on one pair of input, those I will present now, but you should
  know them if you are familiar with HTM:
  <ul>
  <li>Forward Input [f]:
      <ol><li>Size of the input [n of f]</li><li>Number of active inputs [w of f] </li></ol>
  <li>
  <li>Context Input [c]:
      <ol><li>Size of the input [n of c]</li><li>Number of active inputs [w of c] </li></ol>
  <li>
  <li>Feedback Input [b]:
      <ol><li>Size of the input [n of b]</li><li>Number of active inputs [w of b] </li></ol>
  <li>
  </ol>
